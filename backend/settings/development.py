from .base import *
from pathlib import Path
import dotenv
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

dotenv_file = os.path.join(BASE_DIR, ".env")
print(dotenv_file)
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

SIMPLE_JWT.update({
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": "",
})

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

CORS_ORIGIN_WHITELIST = [
    # os.environ.get('CORS_ORIGIN_WHITELIST').split(' ')
]
