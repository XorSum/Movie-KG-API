import jwt
import time
from utils.json_response import json_response
from MovieKgAPI.settings.base import JWT_CONFIG


def encode(payload):
    """
    Encode an payload into token
    dict:param payload: data
    str:return: token
    """
    return jwt.encode(payload, JWT_CONFIG['SECRETE_KEY'],
                      JWT_CONFIG['ALGORITHM']).decode('utf-8')


def decode(token):
    """
    Decode an token
    str:param token:
    dict:return:
    """
    try:
        ret = jwt.decode(token, JWT_CONFIG['SECRETE_KEY'], JWT_CONFIG['ALGORITHM'])
    except Exception:
        return None
    return ret


def login_required(func):
    def wrapper(requests, *args, **kwargs):
        if 'token' in requests.GET:
            payload = jwt.decode(requests.GET['token'])
            if payload:
                now = time.time()
                if float(payload['valid_date']) <= now:
                    requests.GET['token'] = payload['username']
                    return func(requests, *args, **kwargs)
        return json_response(None, 401)
    return wrapper
