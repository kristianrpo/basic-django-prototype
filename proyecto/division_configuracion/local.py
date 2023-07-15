from .base import *
DEBUG = True

ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'proyecto_1',
        'USER' : 'kristianrpo',
        'PASSWORD' : 'Youtube30102004.',
        'HOST' : 'localhost',
        'PORT' : '5432'
    }
}
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]
MEDIA_URL = 'media/'
MEDIA_ROOT = [BASE_DIR.child('media')]