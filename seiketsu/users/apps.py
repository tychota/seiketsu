from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'seiketsu.users'
    verbose_name = "Users"

    def ready(self):
        pass
