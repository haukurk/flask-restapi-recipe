__author__ = 'haukurk'


def log_exception(sender, exception, **extra):
    """
    Log an exception to our logging framework.
    @param sender: sender
    @param exception: exception triggered
    @**extra: other params.
    @return: void
    """
    sender.logger.debug('Got exception during processing: %s', exception)


def error_incorrect_version(version):
    """
    Return a response when the client is using incorrect API version.
    @param version: version in use.
    @return: dict
    """
    return {"status": "error", "message": "incorrect API version "+str(version)+" used."}


def error_object_not_found():
    """
    Return an error response when something is not found, like a object in a database.
    @return: dict
    """
    return {"status": "error", "message": "object not found"}


def error_commit_error(ex):
    """
    Return an error response when database commit fails somehow.
    Like when inserting into a database and you get a unique constraint violated.
    @return: dict
    """
    return {"status": "error", "message": "error when committing object to database", "exception": ex.message}