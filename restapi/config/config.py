__author__ = 'haukurk'


class DefaultConfig(object):
    """
    Default Config (Is used when RESTAPICONFIG environment variable is not set)
    """
    APP_NAME = 'rest-api'
    DEBUG = False
    LOG_LEVEL = 'WARNING'
    LOG_DIR = 'logs/'
    SQLALCHEMY_DATABASE_URI = "sqlite:///database/api.db"
    SECRET_KEY = "Ch4ng3M3!"


class Development(DefaultConfig):
    """
    Config class for development.
    """
    DEBUG = True
    LOG_LEVEL = 'INFO'
    SQLALCHEMY_DATABASE_URI = "sqlite:///database/api_test.db"


class UnitTesting(DefaultConfig):
    """
    Config class for unittests
    """
    DEBUG = True
    LOG_LEVEL = 'INFO'
    LOG_DIR = '../logs/'
    SQLALCHEMY_DATABASE_URI = "sqlite:///database/api_unittest.db"