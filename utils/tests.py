"""
I tried using django.test.TestCase, but...
It doesn't work, maybe is this file isn't under an app?
Also, this file can't run successfully.
Just ignore it please. :(
"""
import time
from utils import JWT


def test_jwt():
    data = {
        'username': 'hantiaotiao',
        'valid_date': time.time()
    }
    token = JWT.encode(data)
    payload = JWT.decode(token)
    assert payload == data


if __name__ == '__main__':
    test_jwt()
