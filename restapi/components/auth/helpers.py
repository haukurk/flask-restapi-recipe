from restapi.components.auth import model

__author__ = 'haukurk'

import base64
import hashlib
import random


def get_apiauth_object_by_ip(ip):
    """
    Query the datastorage for an API key.
    @param ip: ip address
    @return: apiauth sqlachemy object.
    """
    return model.APIAuth.query.filter_by(ip=ip).first()


def get_apiauth_object_by_key(key):
    """
    Query the datastorage for an API key.
    @param ip: ip address
    @return: apiauth sqlachemy object.
    """
    return model.APIAuth.query.filter_by(key=key).first()


def get_apiauth_object_by_keyid(keyid):
    """
    Query the datastorage for an API key.
    @param ip: ip address
    @return: apiauth sqlachemy object.
    """
    return model.APIAuth.query.filter_by(id=keyid).first()


def get_all_apiauth_object():
    """
    Query the datastorage for all API keys.
    @param ip: ip address
    @return: apiauth sqlachemy object.
    """
    return model.APIAuth.query.all()


def generate_hash_key():
    """
    @return: A hashkey for use to authenticate agains the API.
    """
    return base64.b64encode(hashlib.sha256(str(random.getrandbits(256))).digest(),
                            random.choice(['rA', 'aZ', 'gQ', 'hH', 'hG', 'aR', 'DD'])).rstrip('==')