import jwt
import json
import time
from utils.json_response import json_response
from MovieKgAPI.settings.base import JWT_CONFIG


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
    def wrapper(requests, *args, **kwargs):
        if 'token' in requests.GET:
            requests.GET = requests.GET.copy()
            payload = decode(requests.GET['token'])
            if payload:
                now = time.time()
                if float(payload['valid_date']) <= now:
                    requests.GET['token'] = payload['username']
                    return func(requests, *args, **kwargs)
        return json_response(None, 401)
    return wrapper
