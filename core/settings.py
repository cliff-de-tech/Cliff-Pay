"""
Django settings for core project.
"""
import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv
from django.core.exceptions import ImproperlyConfigured

# Load environment variables
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Debug Mode - Must be defined early as it's used in other settings
DEBUG = os.environ.get('DEBUG') == 'True'

# --- SECURITY SETTINGS ---
SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY:
    if DEBUG:
        # Development-only fallback
        SECRET_KEY = 'django-insecure-dev-key-change-this-in-production'
    else:
        raise ImproperlyConfigured(
            'SECRET_KEY environment variable is required. '
            'Set it in your .env file or environment.'
        )

# ALLOWED_HOSTS: Load from environment with proper security defaults
allowed_hosts_env = os.environ.get('ALLOWED_HOSTS')
if allowed_hosts_env:
    ALLOWED_HOSTS = [
        host.strip()
        for host in allowed_hosts_env.split(',')
        if host.strip()
    ]
elif DEBUG:
    # In development, default to allowing all hosts
    ALLOWED_HOSTS = ['*']
else:
    # In production, require ALLOWED_HOSTS to be explicitly set
    raise ImproperlyConfigured(
        'ALLOWED_HOSTS environment variable is required in production. '
        'Set it to a comma-separated list of allowed hosts in your .env file or environment.'
    )

# Application definition
INSTALLED_APPS = [
    'accounts',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases


DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{(BASE_DIR / "db.sqlite3").as_posix()}',
        conn_max_age=600
    )
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = 'static/'

# Custom User Model
AUTH_USER_MODEL = 'accounts.CustomUser'