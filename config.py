import os
import vars
import datetime

class BaseConfig(object):
    SECRET_KEY                          = os.environ['secretKey']
    SIJAX_STATIC_PATH                   = os.path.join('.', os.path.dirname(__file__), 'app/static/js/sijax/')
    SIJAX_JSON_URI                      = 'app/static/js/sijax/json2.js'
    JSON_AS_ASCII                       = False
    TEMPLATES_AUTO_RELOAD               = True
    PERMANENT_SESSION_LIFETIME          = datetime.timedelta(hours=4)

class DevelopmentConfig(BaseConfig):
    DEBUG                               = True
    TESTING                             = False