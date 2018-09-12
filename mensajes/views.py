from django.http import HttpResponse
import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Messege

def index(request):
    messege_list = Messege.objects.order_by('-pub_date')
    ip_client = request.META.get('REMOTE_ADDR')

    now = datetime.datetime.now()
    context = {
            'messege_list': messege_list,
            'ip_client': ip_client,
            'time': now
        }
    return render(request, 'mensajes/index.html', context)

def new(request):
    n = request.POST.get('messege','')
    i = request.POST.get('client_ip','')
    t = request.POST.get('pub_date','')
    nuevo = Messege(messege=n, pub_date=t, client_ip=i)
    nuevo.save()
    return redirect('/mensajes/')
