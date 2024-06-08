from decouple import config

from .base import *

DEBUG = config("DEBUG", default=False, cast=bool)


ALLOWED_HOSTS = []
