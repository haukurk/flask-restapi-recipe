__author__ = 'haukurk'


def log_exception(sender, exception, **extra):
    """ Log an exception to our logging framework """
    sender.logger.debug('Got exception during processing: %s', exception)


def error_incorrect_version(version):
    """
    @param version: version in use.
    @return: dict
    """
    return {"status": "error", "message": "incorrect API version "+str(version)+" used."}


def error_object_not_found():
    """

    """
    return {"status": "error", "message": "object not found"}


def error_commit_error():
    """

    """
    return {"status": "error", "message": "error when committing object to database"}