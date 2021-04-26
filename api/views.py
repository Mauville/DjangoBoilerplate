import requests
from django.conf import settings
from django.http import HttpResponse, JsonResponse, FileResponse
from django.shortcuts import redirect

endpoint = 'http://localhost:3030/archive' if settings.DEBUG else 'http://sparql.semantyk.com:3030/archive'


def register(response):
    return HttpResponse(response)
