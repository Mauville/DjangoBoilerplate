from django.http import HttpResponse, JsonResponse, FileResponse


def register(response):
    return HttpResponse(response)
