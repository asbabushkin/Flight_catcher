import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent   # Flight_catcher_web/flight_catcher

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "backend"]
CSRF_TRUSTED_ORIGINS = [
    "https://103.90.73.189",
    "http://103.90.73.189",
    "https://127.0.0.1",
    "http://127.0.0.1",
    "https://localhost",
    "http://localhost",
    "https://*.aviaspy.ru",
    "http://*.aviaspy.ru"
]
CORS_ORIGIN_ALLOW_ALL = True

INSTALLED_APPS = [
    # Django Applications
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third-party Applications
    "corsheaders",
    # Project Applications
    "flight_catcher",
    "flight_search.apps.FlightSearchConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "flight_catcher.urls"

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

WSGI_APPLICATION = "flight_catcher.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("HOST"),
        "PORT": os.getenv("PORT"),
    }
}

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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': 'debug.log'
        }
    },
    '': {
        'django': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
            'propagate': True
        },
        'django.request': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        },
        'django.server': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        },
        'django.db.backends': {
            'level': 'WARNING',
            'handlers': ['console', 'file']
        },
        'django.security.*': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        }
    }
}

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_TZ = True

USE_L10N = True

DATE_INPUT_FORMATS = ("%d/%m/%Y", "%Y/%m/%d")


# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR.joinpath("static")


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
