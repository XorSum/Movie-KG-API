from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'User'

    def ready(self):
        from User.models import Article
        from User.models import Favorites
        from User.models import ReadHistory
        from User.models import User
        from User.models import UserManager
