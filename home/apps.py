"""This file is used to configure the app name."""
from django.apps import AppConfig

class HomeConfig(AppConfig):
    """
    Home app configuration.

    Attributes:
        default_auto_field (str): The default auto field for the models.
        name (str): The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
