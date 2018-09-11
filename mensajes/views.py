from django.http import HttpResponse
import datetime

def index(request):
    now = datetime.datetime.now()
    html = "<html><body> %s:%s:%s </body></html>" % (now.hour, now.minute, now.second)
    return HttpResponse(request.META.get('REMOTE_ADDR') + html)
    # HTTP_X_FORWARDED_FOR
