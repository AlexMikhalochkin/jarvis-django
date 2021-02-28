import json
import logging
import urllib

from django.http import JsonResponse
from django.shortcuts import redirect

logger = logging.getLogger('logger')


def auth(request):
    state = request.GET.get('state')
    response_type = request.GET.get('response_type')
    redirect_uri = request.GET.get('redirect_uri')
    client_id = request.GET.get('client_id')
    params = {'state': state, 'code': '711ecb4f-200b-406b-967b-1b1db0953bd8'}
    return redirect(redirect_uri + '?' + urllib.parse.urlencode(params))


def token(request):
    client_secret = request.POST.get('client_secret')
    client_id = request.POST.get('client_id')
    grant_type = request.POST.get('grant_type')
    redirect_uri = request.POST.get('redirect_uri')
    refresh_token = request.POST.get('refresh_token')
    code = request.POST.get('code')
    response = {
        'access_token': 'ca3e4771-a0e8-4de3-ba63-a3545d15bfb2',
        'token_type': 'bearer',
        'refresh_token': '5d8rr9d7-a988-0a45-955c-74068fh8ur0l',
        'scope': 'x:devices:* r:devices:*',
        'expires_in': '1576799999'
    }
    return JsonResponse(response)


def handle(request):
    body = json.loads(request.body.decode('utf-8'))
    logger.error(body)
    headers = body['headers']
    interaction_type = headers['interactionType']
    response = {}
    interaction_response = ''
    if 'discoveryRequest' == interaction_type:
        interaction_response = 'discoveryResponse'
        response['requestGrantCallbackAccess'] = 'true'
        device = {
            'externalDeviceId': 'kitchen-light-0',
            'deviceCookie': {'updatedcookie': 'old or new value'},
            'friendlyName': 'Kitchen Bulb',
            'manufacturerInfo': {
                'manufacturerName': 'LIFX',
                'modelName': 'A19 Color Bulb'
            },
            'deviceHandlerType': 'c2c-rgbw-color-bulb',
            'deviceUniqueId': 'unique identifier of device',
            'deviceContext': {
                'roomName': 'Kitchen',
                'groups': ['Kitchen Lights', 'House Bulbs'],
                'categories': ['light', 'switch']
            }

        }
        response['devices'] = [device]

    response['headers'] = {
        'schema', 'st-schema',
        'version', '1.0',
        'interactionType', interaction_response,
        'requestId', headers['requestId']
    }
    return JsonResponse(response)
