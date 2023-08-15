"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
class ImproperlyConfigured(Exception):
    """
    Exception raised for improper configuration or missing settings.
    """
    def __init__(self, message=None, *args, **kwargs):
        if message is None:
            message = "Improperly configured."
        super().__init__(message, *args, **kwargs)

def get_env_variable(var_name):
  try:
    return os.environ[var_name]
  except KeyError:
    error_msg = 'Set the {} environment variable'.format(var_name)
    raise ImproperlyConfigured(error_msg)

SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'travels',
    'reviews',
    'rest_framework',
    'storages',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', 
    'django.middleware.security.SecurityMiddleware', #이거랑
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware', #이거랑
    'django.contrib.auth.middleware.AuthenticationMiddleware', #이거
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
# 		'NAME': get_env_variable('DATABASE'),
#         'USER': get_env_variable('DB_USER'),
#         'PASSWORD': get_env_variable('DB_PASSWORD'),
#         'HOST': get_env_variable('DB_HOST'),
#         'PORT': get_env_variable('DB_PORT'),
#         'OPTIONS':{
#             'init_command' : "SET sql_mode='STRICT_TRANS_TABLES'"
#         }
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# AWS S3
AWS_ACCESS_KEY_ID = 'AKIA6BTTBQPRVQ4IM65J'
AWS_STORAGE_BUCKET_NAME = 'likeliionthrowback'
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_S3_CUSTOM_DOMAIN = 'likeliionthrowback.s3.amazonaws.com' 
AWS_DEFAULT_ACL = 'public-read'  # or use 'private' based on your need
AWS_QUERYSTRING_AUTH = False

AWS_STATIC_LOCATION = 'static'
STATIC_URL = "https://likeliionthrowback.s3.ap-northeast-2.amazonaws.com/%ED%85%8C%EC%8A%A4%ED%8A%B8+%EC%82%AC%EC%A7%84/" 
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_MEDIA_LOCATION = 'media'
MEDIA_URL = "https://likeliionthrowback.s3.ap-northeast-2.amazonaws.com/Media/" 
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# import socket
# def get_ipaddress():
#     host_name = socket.gethostname()
#     ip_address = socket.gethostbyname(host_name)
#     return "https://"+ip_address

CSRF_TRUSTED_ORIGINS = ["https://port-0-throwback-eu1k2lllcfh9do.sel3.cloudtype.app/"]