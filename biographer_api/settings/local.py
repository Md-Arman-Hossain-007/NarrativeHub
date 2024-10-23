from .base import *
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
        "DJANGO_SECRET_KEY",
        default="XXgyo8OVUPGLK3wm6drzlzx3mLIIYEoWa_71qyAs-8oGtrDtrgw",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]
ALLOWED_HOSTS = ["localhost"]
CORS_ALLOWED_ORIGINS = ["http://localhost:8080"]

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "support@biographer_api.site"
DOMAIN = env("DOMAIN")
SITE_NAME = "Biographer Haven"
