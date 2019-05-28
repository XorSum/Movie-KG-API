from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, nickname, password=None):
        """
        Create user in db
        :param username:
        :param nickname:
        :param password:
        :return:
        """
        def valid(__username):
            """
            Check username is valid
            :param __username:
            :return: True / False
            """
            if not __username:
                return False
            if not __username[0].islower():
                return False
            for ch in __username:
                if not (ch.islower() or ch.isdigit()):
                    return False
            return True

        if not valid(username):
            raise ValueError('用户名必须由小写字母和数字组成，且开头为小写字母')

        user = self.model(
            username=username,
            nickname=nickname,
        )

        user.set_password(password)
        user.save(using=self._db)
        user.following.add(user)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, nickname, password):
        """
        Create a normal user first, then set it administrator
        :param username:
        :param nickname:
        :param password:
        :return:
        """
        user = self.create_user(
            username=username,
            nickname=nickname,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
