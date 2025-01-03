"""
Django settings for UNet project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

PRIVATE_KEY = "-----BEGIN RSA PRIVATE KEY-----\nMIICWwIBAAKBgQDceMDSQGhv7t4AInvtU41k+NdoUvodaNxb4JqqBfwPH9OnHqLg\n+CsQSKOoHn2ysX9Npv/NZwp/pw5z+I92gvjLan8Zdk3UCnR0jUcAw2qxtQseYLoj\nN3Wr/xsnU/48LR1FU9Uc6TF3kbPRmsut2+m6rz8/FXI0YyMth3jsX4i3nQIDAQAB\nAoGAY4XfBQouGtkpPcZTSv68hSgPlPhgD4aWcqMhLj8lWW50jKw3unZMej1QI0Qg\nWdnmLZeFQaOSCa3PyGob2NOmmtX8Z5+1OW/MhhHSoOINNTyTayAbOIxmy1GSmM78\nP+m5mxX8+ufSD6VCXJh1IRb2ccNeoR1Plx8h1YxGQye0IgECQQD3lZiccDLUhSOe\n1adIH56jFdUlOXc1PRfQuLgupVWGL822EpX1xnDwPiHVI5tjb4WGVRKA9VTeHGUP\nlZYvjBCpAkEA4/c7GrBqM4eQW3f4zP9HCzzMu4RV0ycRIc2lRHSZ5bP3sGGaJ4Cy\nzZviNsIEzC0m8+I+VlDx8elj97dzshHj1QJAZkxqlWEKr6Mfd7ah+vwNqScRPeND\nrTzEBVr9x1BLSTmhTvTY/4dyDOIvSoj+4JQo4Ltv/NbhrTCgVVMijhzamQJAb7ok\nBZig9FBkt++8yPv0XdWWofDh/3MOOnsHnN1o7+OcaZ3sZ5/0AkF8RUoh/8/BX5Zq\n5vMVIXM5w5bt5UBPYQJAbnUppucTYoXQx66cvP/DQWNAngEOxVREJ1LtMAprq7KD\nPbS5c261+AX2bxyS7shwuqoKGSX4aFUr1ZJtB1+Axw==\n-----END RSA PRIVATE KEY-----\n"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2em2oo&eh)c13zodczrd&)2x(0211_#6a9hy)!e^u-n9aep_s8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

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
    'ngos',
    'donations',
    'projects',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'payments',
]

AUTHENTICATION_BACKENDS = [
    'users.authentication_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',  # Fallback to default
]


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',  # Use JSON responses by default
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'UNet.urls'

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

WSGI_APPLICATION = 'UNet.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'unet',  # Replace with your database name
        'USER': 'postgres',       # Replace with your PostgreSQL username
        'PASSWORD': 'root',   # Replace with your PostgreSQL password
        'HOST': '127.0.0.1',           # Set to 'localhost' if running locally
        'PORT': '5432',                # Default PostgreSQL port
    }
}

# settings.py
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=360),  # Adjust as needed
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
}



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'shruthisdustbin@gmail.com' #to email, please change it later!! i didnt have any other spare testing email domains
EMAIL_HOST_PASSWORD = 'iflv rovi zwip hvss' #app password, can be generated in google after setting up 2FA for that account

