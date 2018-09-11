from django.http import HttpResponse


def index(request):
    return HttpResponse(request.META.get('REMOTE_ADDR'))
