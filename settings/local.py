from .common import *
import logging
MEDIA_URL = "https://uat.taiga.calendar.ly/media/"
STATIC_URL = "https://uat.taiga.calendar.ly/static/"
SITES["front"]["scheme"] = "https"
SITES["front"]["domain"] = "uat.taiga.calendar.ly"

SECRET_KEY = "t&&r8(j-7l$@2yn!a5xpimv%zda()qadyblee&e#9mkdbb*5&a"

DEBUG = False
PUBLIC_REGISTER_ENABLED = True

DEFAULT_FROM_EMAIL = "no-reply@uat.taiga.calendar.ly"
SERVER_EMAIL = DEFAULT_FROM_EMAIL

#Loggly
LOGGING = {
   'version': 1,
   'disable_existing_loggers': False,
   'formatters': {
      'django': { 
         'format':'django: %(message)s',
       },
    },

   'handlers': {
      'logging.handlers.SysLogHandler': {
         'level': 'DEBUG',
         'class': 'logging.handlers.SysLogHandler',
         'facility': 'local7',
         'formatter': 'django',
         'address' : '/dev/log',
       },
   },

   'loggers': {
      'loggly_logs':{
         'handlers': ['logging.handlers.SysLogHandler'],
         'propagate': True,
         'format':'django: %(message)s',
         'level': 'DEBUG',
       },
    }
}
#CELERY_ENABLED = True

EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
EVENTS_PUSH_BACKEND_OPTIONS = {"url": "amqp://taiga:PASSWORD_FOR_EVENTS@localhost:5672/taiga"}

# Uncomment and populate with proper connection parameters
# for enable email sending. EMAIL_HOST_USER should end by @domain.tld
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = "localhost"
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_PORT = 25

# Uncomment and populate with proper connection parameters
# for enable github login/singin.
#GITHUB_API_CLIENT_ID = "yourgithubclientid"
#GITHUB_API_CLIENT_SECRET = "yourgithubclientsecret"



logger = logging.getLogger('loggly_logs')
logger.info('Hi, Welcome to Loggly.')
