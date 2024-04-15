from pathlib import Path
from dotenv import load_dotenv
from datetime import timedelta
import os

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(f"{BASE_DIR}/.env")

getValue = lambda key: os.environ.get(key)

ENV_VARS = [
    "ENVIRONMENT",
    "DJANGO_SECRET_KEY",
    "DJANGO_JWT_SIGNING_KEY",
    "DJANGO_JWT_ALGORITHM",
    "DJANGO_JWT_LIFETIME",
    "DJANGO_BACKEND_URL",
    "DJANGO_DEBUG",
    "VITE_BACKEND_URL",
    "GMAP_SECRET",
    "GEMINI_API",
]

loaded = True
for item in ENV_VARS:
    if not getValue(item):
        print(f"Environment variable '{item}' not loaded.")
        loaded = False
if not loaded:
    exit()

GEMINI_API = getValue("GEMINI_API")

SECRET_KEY = getValue("DJANGO_SECRET_KEY")

DEBUG = bool(getValue("DJANGO_DEBUG"))

SITE_ID = 1

ACCOUNT_EMAIL_VERIFICATION = "none"

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = [
    "https://studybuddybe.up.railway.app",
    "https://studybuddyswe.vercel.app",
]

INSTALLED_APPS = [
    "corsheaders",

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.admindocs",

    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",

    "allauth",
    "allauth.account",
    "allauth.socialaccount",

    "dj_rest_auth",
    "dj_rest_auth.registration",
    
    'bookings.apps.BookingsConfig',
    'carts.apps.CartsConfig',
    'orders.apps.OrdersConfig',
    'products.apps.ProductsConfig',
    'profiles.apps.ProfilesConfig',
    'study_areas.apps.StudyAreasConfig',
    'buddy.apps.BuddyConfig'
]

LIFETIME = int(getValue("DJANGO_JWT_LIFETIME"))

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=LIFETIME),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=LIFETIME),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": True,
    "SIGNING_KEY": getValue("DJANGO_JWT_SIGNING_KEY"), 
    "ALGORITHM": getValue("DJANGO_JWT_ALGORITHM"),
}

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 1000,
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

REST_AUTH = {
    "USE_JWT": True,
    "JWT_AUTH_HTTPONLY": False,
}

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django.contrib.admindocs.middleware.XViewMiddleware",
]

ROOT_URLCONF = 'project.urls'

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

WSGI_APPLICATION = 'project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CORS_ALLOW_ALL_ORIGINS = True

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Singapore'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATIC_ROOT = f'{BASE_DIR}/static/'

MEDIA_URL = 'media/'

MEDIA_ROOT = f'{BASE_DIR}/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
