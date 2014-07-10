__author__ = 'haukurk'

from functools import wraps
from flask import request, abort, Response
from restapi.components.auth.helpers import get_apiauth_object_by_key
from restapi import log, log_to_file


def match_api_keys(key, ip):
    """
    Match API keys and discard ip
    @param key: API key from request
    @param ip: remote host IP to match the key.
    @return: boolean
    """
    if key is None or ip is None:
        return False
    api_key = get_apiauth_object_by_key(key)
    if api_key is None:
        return False
    elif api_key.ip == "0.0.0.0":   # 0.0.0.0 means all IPs.
        return True
    elif api_key.key == key and api_key.ip == ip:
        return True
    return False


def require_app_key(f):
    """
    @param f: flask function
    @return: decorator, return the wrapped function or abort json object.
    """

    @wraps(f)
    def decorated(*args, **kwargs):
        if match_api_keys(request.args.get('key'), request.remote_addr):
            return f(*args, **kwargs)
        else:
            with log_to_file:
                log.warning("Unauthorized address trying to use API: " + request.remote_addr)
            abort(401)

    return decorated


## Test HTTP Basic auth

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'samskip' and password == 'owns'


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)

    return decorated
