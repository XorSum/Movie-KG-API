import json

import jwt
import time

from django.core.exceptions import ObjectDoesNotExist

from User.models import User
from utils.json_response import json_response
from MovieKgAPI.settings.base import JWT_CONFIG
from django.shortcuts import get_object_or_404

def post(func):
    def wrapper(requests, *args, **kwargs):
        requests.POST = json.loads(requests.body.decode('utf-8'))
        return func(requests, *args, **kwargs)
    return wrapper

def encode(user):
    """
    Encode an payload into token
    dict:param payload: data
    str:return: token
    """
    return jwt.encode({
        'username': user.username,
        'valid_date': time.time() + JWT_CONFIG['TIME_OUT'],
    }, JWT_CONFIG['SECRET_KEY'], JWT_CONFIG['ALGORITHM']).decode('utf-8')


def decode(token):
    """
    Decode an token
    str:param token:
    dict:return:
    """
    try:
        ret = jwt.decode(token, JWT_CONFIG['SECRET_KEY'], JWT_CONFIG['ALGORITHM'])
    except Exception:
        return None
    return ret


def login_required(func):
    """
    在request.GET或者request.POST中拿到token,检查，然后将合法user放到requests.GET['user']
    :param func:
    :return:
    """
    def wrapper(requests, *args, **kwargs):
        token = requests.GET.get('token',None)
        if token == None:
            token = requests.POST.get('token',None)
        if token == None:
            return json_response(None, 400,'token needed')
        payload = decode(token)
        if payload:
            now = time.time()
            if float(payload['valid_date']) >= now:
                user = get_object_or_404(User,username=payload['username'])
                requests.GET = requests.GET.copy()
                requests.GET['user'] = user
                return func(requests, *args, **kwargs)
            else:
                return json_response(None, 401, 'Out Of Time')
        else:
            return json_response(None, 400,'invalid token')
    return wrapper
