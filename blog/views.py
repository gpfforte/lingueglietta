from django.shortcuts import render
from datetime import datetime
from .models import Post
# Create your views here.
def index(request):
    now = datetime.now()
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    context={"now": now, "num_visits": num_visits}

    return render(request, 'index.html', context=context)



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/blog_home.html', context=context)


def about(request):
    return render(request, 'blog/blog_about.html', {'title': 'About'})

def poesia(request):

    return render(request, 'poesia.html')

def percorsi(request):

    return render(request, 'percorsi.html')