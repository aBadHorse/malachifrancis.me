from .base import *

DEBUG = False
ENV_LABEL = 'prod'
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# postgres database: mfdotmedb
# postgres user: mfdotmeuser
# mfdotmeuser pw: 85zh98CvnhNADrtTfqi75m4vbqVMJZ3v
# postgres su pw: bLCeMS9MkCqppVY
# postgres address: malachifrancis-1165.postgres.pythonanywhere-services.com
# postgres port: 11165
# postgres superuser role name: super

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mfdotmedb',
        'USER': 'mfdotmeuser',
        'PASSWORD': '85zh98CvnhNADrtTfqi75m4vbqVMJZ3v',
        'HOST': 'malachifrancis-1165.postgres.pythonanywhere-services.com',
        'PORT': 11165
    }
}