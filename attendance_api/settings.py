"""
Django settings for attendance_api project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-^qo=vav5z3)i5sxw2ducvfd*4(00yqk28hd0l08!+fqzv=(4pn"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'corsheaders',
    'rest_framework',
    'base'
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = "attendance_api.urls"

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

WSGI_APPLICATION = "attendance_api.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Actual directory user files go to
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# URL used to access the media

MEDIA_URL = '/media/'

DATA_UPLOAD_MAX_NUMBER_FIELDS = None
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:8000",
    "http://192.168.1.14:8000",  # لمحاكي Android
    "http://192.168.1.4:8000",   # استبدليه بعنوان IP لجهازك
]


# settings.py

# List of allowed file extensions
ALLOWED_EXTENSIONS = [
    'bmp', 'dib', 'gif', 'jfif', 'jpe', 'jpg', 'jpeg', 'pbm', 'pgm', 'ppm', 'pnm', 'pfm',
    'png', 'apng', 'tif', 'tiff', 'blp', 'bufr', 'cur', 'pcx', 'dcx', 'dds', 'ps', 'eps',
    'fit', 'fits', 'fli', 'flc', 'ftc', 'ftu', 'gbr', 'grib', 'h5', 'hdf', 'jp2', 'j2k',
    'jpc', 'jpf', 'jpx', 'j2c', 'icns', 'ico', 'im', 'iim', 'mpg', 'mpeg', 'mpo', 'msp',
    'palm', 'pcd', 'pdf', 'pxr', 'psd', 'qoi', 'bw', 'rgb', 'rgba', 'sgi', 'ras', 'tga',
    'icb', 'vda', 'vst', 'webp', 'wmf', 'emf', 'xbm', 'xpm',
]

# Allow .jpg files in addition to the defaults
ALLOWED_EXTENSIONS.append('jpg')
ALLOWED_EXTENSIONS.append('jpeg')  # You may also add 'jpeg' if necessary

# Update the Django setting to allow these extensions
FILE_UPLOAD_ALLOWED_EXTENSIONS = ALLOWED_EXTENSIONS
