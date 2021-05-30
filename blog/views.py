from django.shortcuts import render
from datetime import datetime
from .models import Post
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
# Create your views here.

class PostListView(generic.ListView):
    model = Post
    ordering = ['-date_posted']
    fields = "__all__"
    paginate_by = 10

class PostDetailView(generic.DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

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