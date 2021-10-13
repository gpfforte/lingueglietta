"""
Django settings for lingueglietta project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path
import json
from django.contrib.messages import constants as message_constants
import dj_database_url

MESSAGE_TAGS = {
    message_constants.DEBUG: 'alert-primary',
    message_constants.INFO: 'alert-info',
    message_constants.SUCCESS: 'alert-success',
    message_constants.WARNING: 'alert-warning',
    message_constants.ERROR: 'alert-danger',
}
MESSAGE_LEVEL = message_constants.DEBUG

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

#

DJANGO_DEBUG_KEY = os.environ.get("DJANGO_DEBUG_KEY")

if DJANGO_DEBUG_KEY == "True":
    DEBUG = True
else:
    DEBUG = False


ALLOWED_HOSTS = ["www.lingueglietta.it", "www.lingueglietta.com", ".lingueglietta.com", ".lingueglietta.it",
                 "172.104.245.4", "localhost", "lingueglietta.herokuapp.com", "lingueglietta.com", "lingueglietta.it"]


# Application definition

INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # Add our new application

    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lingueglietta.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'lingueglietta.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {}
DJANGO_DB_ENGINE = os.environ.get("DJANGO_DB_ENGINE")

if DJANGO_DB_ENGINE == "SQLITE":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Connessione da Carli a DB Postgres su macchina Carli
if DJANGO_DB_ENGINE == "POSTGRESQL_DA_HEROKU_SU_HEROKU":
    # Configurazione che viene utilizzata dalla macchina Heroku per la quale DEBUG == False e Locale == False
    DATABASES['default'] = dj_database_url.config(conn_max_age=600)

# Connessione a db Postgres non da Heroku Connessione da Carli a DB Postgres su macchina Carli
if DJANGO_DB_ENGINE == "LINODEPOSTGRESQL":
    DB_POSTGRESQL_NAME = os.environ.get("DB_POSTGRESQL_NAME")
    DB_POSTGRESQL_USER = os.environ.get("DB_POSTGRESQL_USER")
    DB_POSTGRESQL_PWD = os.environ.get("DB_POSTGRESQL_PWD")
    DB_POSTGRESQL_HOST = os.environ.get("DB_POSTGRESQL_HOST")
    DB_POSTGRESQL_PORT = os.environ.get("DB_POSTGRESQL_PORT")
    # ****************************************
    DATABASES = {

        'default': {

            'ENGINE': "django.db.backends.postgresql_psycopg2",

            'NAME': DB_POSTGRESQL_NAME,

            'USER': DB_POSTGRESQL_USER,

            'PASSWORD': DB_POSTGRESQL_PWD,

            'HOST': DB_POSTGRESQL_HOST,

            'PORT': DB_POSTGRESQL_PORT,

        }

    }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'it-it'

TIME_ZONE = 'Europe/Rome'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'

# if os.environ.get("SERVER_RUNNING") == "LINODE":
#     # Questo serve per scrivere la mail nella console
#     EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
#     EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'email')
#     # EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# else:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get("EMAIL_HOST_SERVER")  # 'smtp.office365.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = os.environ.get("EMAIL_HOST_USER")
SERVER_EMAIL = os.environ.get("EMAIL_HOST_USER")


LOGIN_URL = "/accounts/login"

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'filerotate': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR / 'debug.log',
            'formatter': 'verbose',
            'maxBytes': 1024*1024*15,  # 15MB
            'backupCount': 10,
        },
    },

    'root': {
        'handlers': ['filerotate'],
        'level': 'DEBUG',
    },
    'loggers': {
        'withdrawal': {
            'handlers': ['console', 'filerotate'],
            'level': os.environ.get('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
        'django.request': {
            'handlers': ['console', 'filerotate'],
            'level': os.environ.get('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
        'django.security.DisallowedHost': {
            'handlers': ['console', 'filerotate'],
            'propagate': False,
        },
    },
}
