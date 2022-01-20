from django.shortcuts import render, reverse
from datetime import datetime
from .models import Post, Comment
from .form import CommentForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import FormMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
import logging
logger = logging.getLogger("lingueglietta")
# Create your views here.


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class PostListView(generic.ListView):

    model = Post
    ordering = ['-date_posted']
    fields = "__all__"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        ip_address = get_client_ip(self.request)
        logger.info(str(ip_address)+"-"+str(self.request))
        context = super(PostListView, self).get_context_data(**kwargs)
        return context


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    form_class = CommentForm

    def get_success_url(self):
        ip_address = get_client_ip(self.request)
        logger.info(str(ip_address)+"-"+str(self.request))
        # return reverse('post-list')
        return reverse('post-detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        ip_address = get_client_ip(self.request)
        logger.info(str(ip_address)+"-"+str(self.request))
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        ip_address = get_client_ip(self.request)
        logger.info(str(ip_address)+"-"+str(self.request))
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        ip_address = get_client_ip(self.request)
        logger.info(str(ip_address)+"-"+str(self.request))
        post = self.get_object()
        author = self.request.user
        myform = form.save(commit=False)
        myform.post = post
        myform.author = author
        form.save()
        return super(PostDetailView, self).form_valid(form)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        ip_address = get_client_ip(self.request)
        logger.info(str(ip_address)+"-"+str(self.request))
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        ip_address = get_client_ip(self.request)
        logger.info(str(ip_address)+"-"+str(self.request))
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ip_address = get_client_ip(self.request)
        logger.info(str(ip_address)+"-"+str(self.request))
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')

    def test_func(self):
        ip_address = get_client_ip(self.request)
        logger.info(str(ip_address)+"-"+str(self.request))
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def index(request):
    ip_address = get_client_ip(request)
    logger.info(str(ip_address)+"-"+str(request))
    now = datetime.now()
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    context = {"now": now, "num_visits": num_visits}
    return render(request, 'index.html', context=context)


def about(request):
    ip_address = get_client_ip(request)
    logger.info(str(ip_address)+"-"+str(request))
    return render(request, 'about.html', {'title': 'About'})


def poesia(request):
    ip_address = get_client_ip(request)
    logger.info(str(ip_address)+"-"+str(request))
    return render(request, 'poesia.html')


def percorsi(request):
    ip_address = get_client_ip(request)
    logger.info(str(ip_address)+"-"+str(request))
    return render(request, 'percorsi.html')

def cappelletta(request):
    ip_address = get_client_ip(request)
    logger.info(str(ip_address)+"-"+str(request))
    return render(request, 'cappelletta.html')