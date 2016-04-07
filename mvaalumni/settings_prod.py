from settings_local import *
from settings_base import *

DEBUG = False
ALLOWED_HOSTS = ['mva-alumni.org']
DOMAIN = 'mva-alumni.org'
WSGI_APPLICATION = 'mvaalumni.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mvaalumni',
        'USER': 'mvaalumni',
        'PASSWORD': DB_PASSWORD,
        'HOST': '',
        'PORT': '',
    }
}

STATIC_ROOT = '/srv/www/mvaalumni/static'
STATIC_URL = '/static/'

MEDIA_ROOT = '/srv/www/mvaalumni/media'
MEDIA_URL = '/media/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_ADMIN = 'root@mva-alumni.org'
EMAIL_CONTACT = 'contact@mva-alumni.org'
EMAIL_NOREPLY = 'no-reply@mva-alumni.org'
EMAIL_TOKEN = 'webmaster@mva-alumni.org'


# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/www/mvaalumni.debug',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}



