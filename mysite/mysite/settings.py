"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import django.core.cache.backends.filebased
import sentry_sdk
from pathlib import Path
from os import getenv
from dotenv import load_dotenv


from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


sentry_sdk.init(
    dsn="https://a4007d9131fa2714d7a4e1ac70986c55@o4506915291529216.ingest.us.sentry.io/4506915300114432",
    traces_sample_rate=1.0,
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "0.0.0.0",
    "127.0.0.1",
]
INTERNAL_IPS = [
    "127.0.0.1",
]

if DEBUG:
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS.append("10.0.2.2")
    INTERNAL_IPS.extend([ip[: ip.rfind(".")] + ".1" for ip in ips])

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admindocs",
    "django.contrib.sitemaps",
    "debug_toolbar",
    "rest_framework",
    "django_filters",
    "drf_spectacular",
    "shopapp.apps.ShopappConfig",
    # 'requestdataapp.apps.RequestdataappConfig',
    "myauth.apps.MyauthConfig",
    "myapiapp.apps.MyapiappConfig",
    "blogapp.apps.BlogappConfig",
    "blogapp_new.apps.BlogappNewConfig",
]

MIDDLEWARE = [
    # "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.admindocs.middleware.XViewMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # "django.middleware.cache.FetchFromCacheMiddleware",
    # 'requestdataapp.middlewares.set_useragent_on_request_middleware',
    # 'requestdataapp.middlewares.CountRequestMiddleware',
    # 'requestdataapp.middlewares.throttling_middleware',
]

ROOT_URLCONF = "mysite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "mysite.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

CACHES = {
    "default": {
        # пустышка:
        # "BACKEND": "django.core.cache.dummy.DummyCache",
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        # Linux:
        # "LOCARION": "/var/tmp/django_cache",
        # Windows:
        "LOCATION": "c:/foo/bar",
    }
}

CACHE_MIDDLEWARE_SECONDS = 200

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

USE_L10N = True

LOCALE_PATHS = [BASE_DIR / "locale"]

# LANGUAGES = (
#     ("en", _("English")),
#     ("ru", _("Russian"))
# )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "uploads"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_REDIRECT_URL = reverse_lazy("myauth:users")

LOGIN_URL = reverse_lazy("myauth:login")

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "My Site Project API",
    "DESCRIPTION": "My site with shop app and custom auth",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}

LOGFILE_NAME = BASE_DIR / "log.txt"
# LOGFILE_SIZE = 400
LOGFILE_SIZE = 1 * 1024 * 1024
LOGFILE_COUNT = 3

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "logfile": {
            # для ротации по дням:
            # "class": "logging.handlers.TimedRotatingFileHandler",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOGFILE_NAME,
            "maxBytes": LOGFILE_SIZE,
            "backupCount": LOGFILE_COUNT,
            "formatter": "verbose",
        },
    },
    "root": {
        "handlers": [
            "console",
            "logfile",
        ],
        "level": "INFO",
    },
}