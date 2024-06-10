import os

from decouple import config

from .base import *

DEBUG = config("DEBUG", default=True, cast=bool)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DATABASE_NAME_LOCAL"),
        "USER": config("DATABASE_USER_LOCAL"),
        "PASSWORD": config("DATABASE_PASSWORD_LOCAL"),
        "HOST": config("DATABASE_HOST_LOCAL", default="localhost"),
        "PORT": config("DATABASE_PORT_LOCAL", default="5432", cast=int),
    }
}

# Media Local Settings
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "ecommerce\\media")
