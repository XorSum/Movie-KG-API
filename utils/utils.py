import json


def get_json_or_none(__object):
    return __object.json() if __object else None


def post(func):
    def wrapper(requests, *args, **kwargs):
        requests.POST = json.loads(requests.body.decode('utf-8'))
        return func(requests, *args, **kwargs)
    return wrapper
