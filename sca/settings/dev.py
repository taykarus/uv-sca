from .base import *
from dotenv import load_dotenv

load_dotenv()

DEBUG = True

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# SQLite Database

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
#     }
# }


# PostgreSQL Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', default='sca'),
        'USER': os.getenv('DB_USER', default='postgres'),
        'PASSWORD': os.getenv('DB_PASSWORD', default='postgres'),
        'HOST': os.getenv('DB_HOST', default='localhost'),
        'PORT': os.getenv('DB_PORT', default=5432),
    }
}
