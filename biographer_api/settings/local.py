from .base import * # noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
        "DJANGO_SECRET_KEY",
        default="XXgyo8OVUPGLK3wm6drzlzx3mLIIYEoWa_71qyAs-8oGtrDtrgw",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CORS_TRUSTED_ORIGINS = ["http://localhost:8080"]