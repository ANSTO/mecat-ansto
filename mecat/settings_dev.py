from settings import *

DEBUG = True

DATABASES = {
    'default': {
        # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tardis_db',
        'USER': 'tardis',
        'PASSWORD': 'tardis',
        'HOST': 'localhost',
        'PORT': '',
    }
}
