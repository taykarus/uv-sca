import dj_database_url

from .base import *


DEBUG = False

ALLOWED_HOSTS = ['taykarus-sca.herokuapp.com']


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config()
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

AWS_STORAGE_BUCKET_NAME = 'taykarus-sca'
AWS_S3_REGION_NAME = 'sa-east-1'

STATICFILES_STORAGE = 'sca.storages.StaticStorage'
DEFAULT_FILE_STORAGE = 'sca.storages.MediaStorage'

AWS_S3_BUCKET_AUTH = True
AWS_S3_MAX_AGE_SECONDS = 60 * 60
AWS_S3_ENCRYPT_KEY = True
