import os


BASE_DIR = os.path.dirname(__file__)

ALLOWED_HOSTS = []

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_9u%s^w(*ejjm3#ea@&!v&dt_tq_8f)tyjq9(h(7!gf1ls_qly'


ROOT_URLCONF = 'melinda.urls'
WSGI_APPLICATION = 'melinda.wsgi.application'

LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True

TIME_ZONE = 'UTC'


STATIC_URL = '/static/'
STATIC_ROOT= '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(BASE_DIR), 'db.sqlite3'),
    }
}


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',   
    'melinda.searchapp',
    'corsheaders',
    'rest_framework',
)


MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
                  
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
     
    'DEFAULT_PERMISSION_CLASSES': [
        # TODO change?
        'rest_framework.permissions.AllowAny',
    ],
}
