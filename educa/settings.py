from pathlib import Path
import oracledb
from decouple import config
import os

oracledb.init_oracle_client(lib_dir="/usr/local/oracle/instantclient_23_3")

ALLOWED_HOSTS = []
BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LANGUAGE_CODE = 'en-us'
# MEDIA_URL = 'media/'
# MEDIA_ROOT = BASE_DIR / 'media'
ROOT_URLCONF = 'educa.urls'
SECRET_KEY = 'django-insecure-(=8y*4^!(z5*dv0b6bx0207vd*682t*b8*as#gjkjd)b5jmxus'
STATIC_URL = 'static/'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
WSGI_APPLICATION = 'educa.wsgi.application'


ORACLE_BUCKET_NAME = os.environ.get('ORACLE_BUCKET_NAME')
ORACLE_BUCKET_NAMESPACE = os.environ.get('ORACLE_BUCKET_NAMESPACE')
ORACLE_REGION = os.environ.get('ORACLE_REGION')

AWS_ACCESS_KEY_ID = os.environ.get('ORACLE_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.environ.get('ORACLE_CUSTOMER_SECRET_KEY')
AWS_STORAGE_BUCKET_NAME = ORACLE_BUCKET_NAME
AWS_S3_CUSTOM_DOMAIN = f"{ORACLE_BUCKET_NAMESPACE}.compat.objectstorage.{ORACLE_REGION}.oraclecloud.com"
AWS_S3_ENDPOINT_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}"
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{ORACLE_BUCKET_NAME}/"


# STATICFILES_STORAGE = 'core.storage_backends.StaticStorage'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'upload/static'),
# ]
# STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{ORACLE_BUCKET_NAME}/static"


INSTALLED_APPS = [
    'courses.apps.CoursesConfig',
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': config('TNS_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
    }
}

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
