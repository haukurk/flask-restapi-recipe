__author__ = 'haukurk'

from functools import wraps


def crossdomain(func, allow_origin=None, allow_headers=None, max_age=None):
    """
    Enable CORS.
    @param func: wrapped function
    @param allow_origin: specify origin
    @param allow_headers: allow headers
    @param max_age: define max age
    @return: function
    """
    if not allow_origin:
        allow_origin = "*"
    if not allow_headers:
        allow_headers = "content-type, accept"
    if not max_age:
        max_age = 60

    @wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        cors_headers = {
            "Access-Control-Allow-Origin": allow_origin,
            "Access-Control-Allow-Methods": func.__name__.upper(),
            "Access-Control-Allow-Headers": allow_headers,
            "Access-Control-Max-Age": max_age,
        }
        if isinstance(response, tuple):
            if len(response) == 3:
                headers = response[-1]
            else:
                headers = {}
            headers.update(cors_headers)
            return response[0], response[1], headers
        else:
            return response, 200, cors_headers
    return wrapper