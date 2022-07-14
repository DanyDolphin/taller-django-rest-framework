'''Users' app config'''

# Django
from django.apps import AppConfig


class UsersConfig(AppConfig):
    '''Users' app config'''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    verbose_name = 'Users'
