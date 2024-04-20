from pathlib import Path

from django.urls import reverse_lazy

# `BASE_DIR` should always point to the `manage.py` directory
BASE_DIR = Path(__file__).resolve().parent.parent
import environ
import dj_database_url

env = environ.Env()
environ.Env.read_env()

SECRET_KEY = "django-insecure-h80@s92%21e^5e+_yib)m3h(b+y+lq#czu**g(+jz8!$^0c+4y"

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '*']

INSTALLED_APPS = [
    # Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party apps

    # Project apps
    "petstagram.common",
    "petstagram.accounts.apps.AccountsConfig",
    "petstagram.photos",
    "petstagram.pets",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "petstagram.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = "petstagram.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "petstagramivan",
#         "USER": "postgres",
#         "PASSWORD": "ggogata43",
#         "HOST": "127.0.0.1",
#         "PORT": "5432",
#     }
# }
DEBUG_PROPAGATE_EXCEPTIONS = True
#
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
#     },
# ]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# URL prefix in the client
STATIC_URL = "static/"

# Directories on the file system
STATICFILES_DIRS = (
    BASE_DIR / "staticfiles",
)

MEDIA_ROOT = BASE_DIR / 'mediafiles'

MEDIA_URL = "/media/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# LOGGING = {
#     'version': 1,
#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         }
#     },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#         }
#     },
#     'loggers': {
#         'django.db.backends': {
#             'level': 'DEBUG',
#             'handlers': ['console'],
#         }
#     }
# }

AUTH_USER_MODEL = 'accounts.PetstagramUser'
LOGIN_REDIRECT_URL = reverse_lazy('home')
LOGOUT_REDIRECT_URL = reverse_lazy('login')

# MAILJET_API_KEY = '211a60c4b5b98b77fade92ea18d312b5'
# MAILJET_SECRET_KEY = 'cb6215db0ed6d001b86131fb94a8d715'
# DEFAULT_FROM_EMAIL = 'ggogata43@gmail.com'

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "gyurovgeorgi740@gmail.com"
EMAIL_HOST_PASSWORD = "vnhmwoauemuqbeyo"

DATABASES = {
    'default': dj_database_url.parse(env('DATABASE_URL'))
}
