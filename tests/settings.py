# -*- coding: utf-8 -*-

import os

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',

    'django_inline_translations',
)

SECRET_KEY = 'test'

TEST_DIR = os.path.dirname(os.path.realpath(__file__))
