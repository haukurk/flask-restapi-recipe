import inspect
import config
from config import *

config_list = inspect.getmembers(config, inspect.isclass)
defined = dict(config_list)