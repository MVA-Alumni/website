from settings_local import *
from settings_base import *

DEBUG = True

ALLOWED_HOSTS = []
DOMAIN = 'localhost:8000'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
MEDIA_URL = '/media/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_ADMIN = 'root@mva-alumni.org'
EMAIL_CONTACT = 'contact@mva-alumni.org'
EMAIL_NOREPLY = 'no-reply@mva-alumni.org'
EMAIL_TOKEN = 'webmaster@mva-alumni.org'
