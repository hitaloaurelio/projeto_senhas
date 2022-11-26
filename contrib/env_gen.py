#!/usr/bin/env python

"""
Django SECRET_KEY generator.
"""
from django.utils.crypto import get_random_string


chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

CONFIG_STRING = """
DEBUG=False
SECRET_KEY= "django-insecure-(@6wgpd2n@@ltot25f=6y%@*xfi!wegjjmo+0u+$j1%ko)ou5n"
ALLOWED_HOSTS=127.0.0.1, .localhost, .vaquejada-teste.herokuapp.com
""".strip() % get_random_string(50, chars)

# Writing our configuration file to '.env'
with open('.env', 'w') as configfile:
    configfile.write(CONFIG_STRING)