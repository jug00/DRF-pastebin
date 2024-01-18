from pathlib import Path
from datetime import timedelta
from environs import Env
import redis

from django.urls import reverse_lazy

# Конфигурация подключения к Redis
REDIS_HOST = 'redis'
REDIS_PORT = 6379
redis_instance = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)

# Инициализация окружения
env = Env()
env.read_env()

# Базовая директория проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Настройки безопасности и отладки
SECRET_KEY = "django-insecure-0#!!pgr%7qa0hj*_8bb#m+h&abl*m_siw$)79e0lhog3*i2heq"
DEBUG = True
ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django.contrib.sites',
    # 3rd party
    "rest_framework",
    "rest_framework.authtoken",
    "django_extensions",
    "rest_framework_simplejwt",
    'rest_framework_simplejwt.token_blacklist',
    'allauth',
    "allauth.account",
    "dj_rest_auth",
    'dj_rest_auth.registration',
    "drf_spectacular",
    "debug_toolbar",
    # Local
    "snippets",
    "accounts"
]

# Промежуточные слои (middleware)
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware"
]

ROOT_URLCONF = "pastebin.urls"

# Настройки шаблонов
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

# WSGI-приложение
WSGI_APPLICATION = "pastebin.wsgi.application"


# Database

DATABASES = {
    "default": env.dj_db_url("DATABASE_URL", default="postgres://postgres@db/postgres")
}

# Password validation
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
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Настройки REST framework
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}


# Настройки электронной почты
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Настройки Simple JWT
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
}

# Настройки кэша
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://redis:6379",
    }
}

# Настройки REST_AUTH
REST_AUTH = {
    'USE_JWT': True,
    'USER_DETAILS_SERIALIZER': 'accounts.serializers.UserSerializer',
    'LOGIN_SERIALIZER': 'accounts.serializers.LoginSerializer',
    "JWT_AUTH_COOKIE": "auth_token",
    'JWT_AUTH_REFRESH_COOKIE': 'refresh_token',
    "JWT_AUTH_COOKIE_USE_CSRF": True,
    "OLD_PASSWORD_FIELD_ENABLED": True,
}

# Настройки allauth
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_CHANGE_EMAIL = True
ACCOUNT_ADAPTER = 'accounts.adapter.AccountAdapter'
LOGIN_URL = reverse_lazy('rest_login')
SITE_ID = 1

# Настройки пользователя
AUTH_USER_MODEL = "accounts.User"

# Настройки для drf-spectacular
SPECTACULAR_SETTINGS = {
    'TITLE': 'Pasta API',
    'DESCRIPTION': 'Project for educational purposes',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

# Настройки Celery для асинхронных задач
CELERY_BROKER_URL = 'amqp://guest:guest@rabbitmq:5672//'


# Настройки для отладочной панели
INTERNAL_IPS = ['127.0.0.1',]
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: True,
}
