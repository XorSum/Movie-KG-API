from users import models as data


def get_user_or_none(username):
    try:
        user = data.User.objects.get(username=username)
    except data.models.ObjectDoesNotExist:
        return None
    return user
