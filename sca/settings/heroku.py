import dj_database_url

from .base import *


DEBUG = True

ALLOWED_HOSTS = ['taykarus-sca.herokuapp.com']


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config()
}
