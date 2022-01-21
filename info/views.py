from django.shortcuts import render
import logging
from blog.views import get_client_ip
logger = logging.getLogger("lingueglietta")
# Create your views here.

def about(request):
    ip_address = get_client_ip(request)
    logger.info(str(ip_address)+"-"+str(request))
    return render(request, 'info/about.html', {'title': 'About'})


def poesia(request):
    ip_address = get_client_ip(request)
    logger.info(str(ip_address)+"-"+str(request))
    return render(request, 'info/poesia.html')


def percorsi(request):
    ip_address = get_client_ip(request)
    logger.info(str(ip_address)+"-"+str(request))
    return render(request, 'info/percorsi.html')

def cappelletta(request):
    ip_address = get_client_ip(request)
    logger.info(str(ip_address)+"-"+str(request))
    return render(request, 'info/cappelletta.html')# Create your views here.

def san_rocco(request):
    ip_address = get_client_ip(request)
    logger.info(str(ip_address)+"-"+str(request))
    return render(request, 'info/san_rocco.html')# Create your views here.

def san_pietro(request):
    ip_address = get_client_ip(request)
    logger.info(str(ip_address)+"-"+str(request))
    return render(request, 'info/san_pietro.html')# Create your views here.