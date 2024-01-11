"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys
# sys.path.append("/Users/apple/Desktop/code/django-app/mysite")

path = '/Users/apple/Desktop/code/django-app/mysite'
if path not in sys.path:
    sys.path.append(path)
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
