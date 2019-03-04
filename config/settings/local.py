from .base import *  # noqa
from .base import env

DEBUG = True

SECRET_KEY = 'p3i_c%)4)hq%9xlwl_zygs^-)4apxw0p!b%-@evd#bg=zuqde)'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += ['debug_toolbar']  # noqa F405
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']  # noqa F405
DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}
INSTALLED_APPS += ['django_extensions']  # noqa F405

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG  # noqa F405
