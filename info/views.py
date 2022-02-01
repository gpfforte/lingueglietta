from django.shortcuts import render
import logging
logger = logging.getLogger("lingueglietta")
# Create your views here.

def about(request):
    return render(request, 'info/about.html', {'title': 'About'})


def poesia(request):
    return render(request, 'info/poesia.html')


def percorsi(request):
    return render(request, 'info/percorsi.html')

def cappelletta(request):
    return render(request, 'info/cappelletta.html')# Create your views here.

def san_rocco(request):
    return render(request, 'info/san_rocco.html')# Create your views here.

def san_pietro(request):
    return render(request, 'info/san_pietro.html')# Create your views here.