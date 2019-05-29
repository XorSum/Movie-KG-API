from django.http import JsonResponse

__INFO = {
    200: {
        'message': 'success',
        'detail': 'Request success',
    },
    201: {
        'message': 'success',
        'detail': 'Create success',
    },
    400: {
        'message': 'invalid',
        'detail': 'Invalid params',
    },
    401: {
        'message': 'forbidden',
        'detail': 'Login required',
    },
    500: {
        'message': 'error',
        'detail': 'Internal error',
    },
    # TODO
}


class NotImplement(Exception):
    pass


def json_response(data, status, token='', detail=''):
    if status not in __INFO:
        raise NotImplement
    return JsonResponse({
        'data': data,
        'status': status,
        'statusInfo': {
            'message': __INFO[status]['message'],
            'detail': __INFO[status]['detail'] if detail == '' else detail,
        },
        'token': token
    })
