activate_this  = '/www/changeme/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
import sys
sys.path.append("/www/changeme/")
from restapi import app as application

