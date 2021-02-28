import logging
import urllib

from django.http import JsonResponse
from django.shortcuts import redirect

logger = logging.getLogger('logger')


def auth(request):
    state = request.POST.get('state')
    response_type = request.POST.get('response_type')
    redirect_uri = request.POST.get('redirect_uri')
    client_id = request.POST.get('client_id')
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
    logger.error(request.body.decode('utf-8'))
    response = {
        'access_token': 'ca3e4771-a0e8-4de3-ba63-a3545d15bfb2',
    }
    return JsonResponse(response)
