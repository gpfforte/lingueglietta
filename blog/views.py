from django.shortcuts import render
from datetime import datetime
from .models import Post
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

class PostList(generic.ListView):
    model = Post
    fields = "__all__"

class PostDetail(generic.DetailView):
    model = Post


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy('blog-home')
    fields = "__all__"
    



# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/post_list.html', context=context)

def index(request):
    now = datetime.now()
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    context={"now": now, "num_visits": num_visits}

    return render(request, 'index.html', context=context)




def about(request):
    return render(request, 'about.html', {'title': 'About'})

def poesia(request):

    return render(request, 'poesia.html')

def percorsi(request):

    return render(request, 'percorsi.html')