__author__ = 'haukurk'

""" Responses that try to follow the JSend specification. """


def create_single_object_response(status, object, object_naming_singular):
    """
    Create a response for one returned object
    @param status: success, error or fail
    @param object: dictionary object
    @param object_naming_singular: name of the object, f.ex. book
    @return: dictionary.
    """
    return {"status": status,
            "data": {
                object_naming_singular: object
            }}


def create_multiple_object_response(status, list_of_objects, objects_naming_plural):
    """
    Create a response for many returned objects
    @param status: success, error or fail
    @param list_of_objects: a list of dictionary objects
    @param objects_naming_plural: name for the object, f.ex. books
    @return: dictionary.
    """
    return {"status": status,
            "data": {
                objects_naming_plural: list_of_objects
            }}


