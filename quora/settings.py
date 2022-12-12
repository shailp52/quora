
from unipath import Path
from decouple import config

PROJECT_DIR = Path(__file__).parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'shail',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '172.17.0.4',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
        'OPTIONS': {
           "init_command": "SET GLOBAL max_connections = 100000", #<-- The fix
        }
    }
}

REDIS_HOST = '172.17.0.3'

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth', 
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    'django_extensions',
    'quora.core',
    'quora.questions',
    'quora.profile',
    'quora.search',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'bootstrap3',
    'crispy_forms',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'quora.urls'

WSGI_APPLICATION = 'quora.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Sao_Paulo'

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('en', 'English'),
    ('pt-br', 'Portuguese'),
    ('es', 'Spanish')
)

LOCALE_PATHS = (PROJECT_DIR.child('locale'), )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
STATIC_ROOT = PROJECT_DIR.parent.child('staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    PROJECT_DIR.child('static'),
)

MEDIA_ROOT = PROJECT_DIR.parent.child('media')
MEDIA_URL = '/media/'

LOGIN_REDIRECT_URL = '/questions/'

ALLOWED_SIGNUP_DOMAINS = ['*']

FILE_UPLOAD_TEMP_DIR = '/tmp/'
FILE_UPLOAD_PERMISSIONS = 644

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            PROJECT_DIR.child('templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
   'django.contrib.auth.backends.ModelBackend',
   'allauth.account.auth_backends.AuthenticationBackend',
)

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

SITE_ID = 4
LOGIN_REDIRECT_URL = '/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'
