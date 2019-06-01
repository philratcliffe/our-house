from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-%we&@o$o+uotuk&p8wc=agmgr-k9j0tg573+n&@*5fvw6nt-a'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar'
]

MIDDLEWARE = MIDDLEWARE + [
    # ...
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # ...
]

INTERNAL_IPS = ('127.0.0.1', '172.17.0.1')

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda r: False,  # disables it
    # '...
}

try:
    from .local import *
except ImportError:
    pass
