"""API app configuration."""    
from django.apps import AppConfig


class ApiConfig(AppConfig):
    """
    Configuration class for the API app.

    Attributes:
        default_auto_field (str): The default auto field for the models.
        name (str): The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
