# coding=utf-8
__version__ = 1.1
version = __version__

import os
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from logbook import Logger
import config
from utils.logging import LoggingSetup, ProductionLoggingSetup

# Start the Flask awesomeness.
app = Flask(__name__)

# Should we use default config (Production) or is it overridden by a environmental variable?
config_name = os.getenv('RESTAPICONFIG',
                        'DefaultConfig')  # Return the value of the environment variable ITAPICONFIG if it exists,
                                    # or "Default" if it doesnt’t. value defaults to None.

# Setup Config
API_CONFIG = config.defined[config_name]
app.config.from_object(API_CONFIG)

# Setup SQLAlchemy
db = SQLAlchemy(app)

# Logging
log = Logger(__name__)
log_setup = ProductionLoggingSetup(app.config['LOG_LEVEL'], app.config['LOG_DIR'] + '%s.log' % app.config['APP_NAME'])
log_to_file = log_setup.get_default_setup()

# Load App Key Auth Decorators
from restapi.components.auth.decorators import require_app_key

## Api routing
# Example Weather Route
from modules.weather import mod as weather_module
app.register_blueprint(weather_module)
# Example Cake Route
from modules.cakes import mod as cakes_module
app.register_blueprint(cakes_module)


"""
Routes that does not matter.
"""


@app.route('/', methods=['GET', 'OPTIONS'])
def api_root():
    """
    Just a route that says hello to the client if he goes to the root of the API. You can remove this if you want.
    """
    body = "Hi, this is a RESTful API." \
           "\n Before using it you should be issued a API key from your friendly developer.."
    return render_template('front.html', content=body, title="Awesome API", version=version)


@app.route("/version", methods=['GET', 'OPTIONS'])
@require_app_key
def api_latest_version():
    """
    Check version of the API, protected with authorization.
    """
    return str(version)

## EOF Routes.

