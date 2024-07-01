"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path
import dotenv

from .auth_password_validators import AUTH_PASSWORD_VALIDATORS
from .databases import DATABASES
from .installed_apps import INSTALLED_APPS
from .JWT import SIMPLE_JWT
from .middleware import MIDDLEWARE
from .rest_framework import REST_FRAMEWORK
from .spectacular import SPECTACULAR_SETTINGS
from .templates import TEMPLATES

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
dotenv.load_dotenv(BASE_DIR / '.env')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS').__str__().split(", ")


# Application definition

INSTALLED_APPS = INSTALLED_APPS

MIDDLEWARE = MIDDLEWARE

REST_FRAMEWORK = REST_FRAMEWORK

ROOT_URLCONF = 'core.urls'

TEMPLATES = TEMPLATES

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = DATABASES


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = AUTH_PASSWORD_VALIDATORS

SIMPLE_JWT = SIMPLE_JWT
# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SPECTACULAR_SETTINGS = SPECTACULAR_SETTINGS
