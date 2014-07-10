__author__ = 'haukurk'

from restapi import db
from restapi.components.auth.helpers import get_apiauth_object_by_ip, generate_hash_key, get_all_apiauth_object, \
    get_apiauth_object_by_keyid
from restapi.components.auth.model import APIAuth


def generate_key(ip, desc):
    """
    Generates a key for an IP address that can authenticate with the API.
    Only one API key for IP.
    @param ip: ip address
    @param desc: description of access
    @return: void
    """
    key = generate_hash_key()
    record = APIAuth(key, ip, desc)
    db.session.add(record)
    db.session.commit()
    print "Issued a key '" + key + "' for the IP '" + ip + "' (" + desc + ") with KEY ID: " + str(record.id)


def delete_key(keyid):
    """
    Deletes an API key for some specific IP.
    @param keyid: KEY ID
    @return: void
    """
    if keyid is None:
        raise Exception("You need to mention a key identity (keyid)")

    api_key = get_apiauth_object_by_keyid(keyid)

    if api_key is not None:
        db.session.delete(api_key)
        db.session.commit()
        print "Revoked API access with the key id " + keyid + " (" + api_key.key + ")"
    else:
        print "This keyid does not exist.."


def show_key(ip):
    """
    Show an API Key for some specific IP.
    @param ip: ip address
    @return: void
    """
    api_key = get_apiauth_object_by_ip(ip)

    if api_key is None:
        print "This IP does not have access.."
    else:
        print "The IP " + str(ip) + " can access the API with the key: " + str(api_key.key)


def show_all_keys():
    """
    Show all API keys for all IPs.
    @return: void
    """
    api_keys = get_all_apiauth_object()

    if api_keys is None:
        print "No one has access.. That's kind of sad for an API."
    else:
        for o in api_keys:
            print "The IP " + str(o.ip) + " has access key " + str(
                o.key) + " API Id: " + str(o.id) + " Description: " + str(o.description)





