import math

from flask import Blueprint, jsonify
import httplib2

from restapi.utils.decorators import crossdomain
from restapi.modules import responses, errors, statuscodes
from restapi.components.auth.decorators import require_app_key
from restapi.utils.conversion import xmltodict
import constants
from restapi.utils import filters

mod = Blueprint('weather', __name__, url_prefix='/api/v<float:version>/weather')

"""
Routes
"""


@mod.route('/<string:woeid>', methods=['GET'])
@crossdomain
@require_app_key
def yahoo_weather(version, woeid):
    """
    Controller for API Function that checks the weather from a woeid
    @param woeid: yahoo woeid
    @return: Response and HTTP code
    """

    # API Version 1.X
    if math.floor(version) == 1:

        url = create_api_url_forecastrss(woeid, True)
        http = httplib2.Http()
        response, content = http.request(url)
        parsed_content = xmltodict.parse(content)
        cleaned_parsed_content = parsed_content["rss"]["channel"]  # Clean out silly structure from yahoo.
        data_content = filters.filter_nested_dicts_values(cleaned_parsed_content, constants.REMOTE_META_KEYS)
        return jsonify(
            responses.create_single_object_response("success", data_content, "weather")), statuscodes.HTTP_OK

    # Unsupported Versions
    else:
        return jsonify(errors.error_incorrect_version(version)), statuscodes.HTTP_VERSION_UNSUPPORTED


from .constants import YAHOO_API_URI

"""
Local Functions
"""


def create_api_url_forecastrss(woeid, celcius):
    """
    Create Full URL for forecastRSS service at yahoo.
    @param woeid: woeid id
    @param celcius: boolean, show celius or not (farenheit)
    @return: string containing full API URL.
    """
    api_url = YAHOO_API_URI
    forecast_url = "?u=c&w=" + woeid if celcius else "?u=f&w=" + woeid
    return api_url + forecast_url