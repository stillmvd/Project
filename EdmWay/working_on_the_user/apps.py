"""
Приложение для сайта EdmWay, работает с пользователем.
"""
from django.apps import AppConfig


class WorkingOnTheUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'working_on_the_user'
    verbose_name = 'Работа с пользователем'