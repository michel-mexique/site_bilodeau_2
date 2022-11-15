"""
Django settings for site_bilodeau_2 project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$1(ht!3jlnsk_sd4m8q$*448xh97@3(6ioz1quz_ar+)a7uf2b'
SITE_ID = 1

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']
INSTALLED_APPS = [

    'home',
    #'conseiller',
    #'blog',
    #'blog_wagtail',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    #Third party
    'django_user_agents',
    'crispy_forms',
    'google_analytics',
    'storages',
    'modelcluster',
    'taggit',
    'captcha',

    #Wagtail
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
]

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

]

ROOT_URLCONF = 'site_bilodeau_2.urls'

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


WSGI_APPLICATION = 'site_bilodeau_2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# LA BASE DE DONNEES EST STOCKEE EN FORMAT SQLITE3
# DANS UN DISQUE AWS LIGHTSAIL QUI A ETE CLONE  
# DANS /home/ubuntu/guides_disk AU LANCEMENT DU SERVEUR
# VOIR https://lightsail.aws.amazon.com/ls/docs/en_us/articles/create-and-attach-additional-block-storage-disks-linux-unix
# ET VOIR LE SCRIPT server_launch_script.py AU
# https://github.com/SDM-FSA-ULaval/site-guides/blob/7746be0e8e9ebadb45a1fc8520478cc59cfd33b0/server_launch_script.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")


MEDIA_ROOT  = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Extra places for collectstatic to find static files.
"""
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
"""

WAGTAIL_SITE_NAME = 'Bilodeau - Gestion de patrimoine'



CRISPY_TEMPLATE_PACK = 'bootstrap4'

#EMAIL 
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # new
EMAIL_HOST = 'smtp.gmail.com' # new


EMAIL_HOST_USER = 'agagnon729@gmail.com' # new
EMAIL_HOST_PASSWORD = 'lncu sblv yppt klpr'#os.environ['EMAIL_HOST_PASSWORD'] # new
EMAIL_PORT = 587 # new
EMAIL_USE_TLS = True # new

"""
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'us-east-2'
"""

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

AWS_ACCESS_KEY_ID = 'AKIAUGDCLOLVXG3GTGMV'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'bucket-6j6w33'

# SI CE PARAMETRE EST True, LE URL SERVI PAR BOT03 CONTIENT UN LIEN 
# AVEC LA AWS ACCESS KEY ID, DONNANT UN LIEN INVALIDE DANS CERTAINES
# REGIONS. VOIR : https://github.com/jschneier/django-storages/issues/687#issuecomment-629223688
AWS_QUERYSTRING_AUTH = False

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

USE_TZ = True
TIME_ZONE = 'EST'

"""
RECAPTCHA_PUBLIC_KEY = os.environ['RECAPTCHA_PUBLIC_KEY']
RECAPTCHA_PRIVATE_KEY = os.environ['RECAPTCHA_PRIVATE_KEY']
"""