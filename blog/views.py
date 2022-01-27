from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
from blog.models import Post, Comment
from .forms import PostForm, CommentForm
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
import logging
logger = logging.getLogger("gpfblog")
# Create your views here.


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


# Create your views here.

class PostListView(generic.ListView):
    model = Post
    ordering = ['-date_posted']
    paginate_by = 10


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    form_class = CommentForm

    def get_success_url(self):
        ip_address = get_client_ip(self.request)
        logger.info(str(ip_address)+"-"+str(self.request))
        # return reverse('post-list')
        return reverse('blog:post-detail', kwargs={'pk': self.object.id})

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
    success_url = reverse_lazy('blog:post-list')
    form_class = PostForm

    def form_valid(self, form):
        ip_address = get_client_ip(self.request)
        logger.info(str(ip_address)+"-"+str(self.request))
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy('blog:post-list')
    form_class = PostForm

    def get_queryset(self):
        ip_address = get_client_ip(self.request)
        logger.info(str(ip_address)+"-"+str(self.request))
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    # success_url = reverse_lazy('blog:post-list')
    form_class = CommentForm

    def get_queryset(self, *args, **kwargs):
        ip_address = get_client_ip(self.request)
        logger.info(str(ip_address)+"-"+str(self.request))
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

    def get_success_url(self):
        ip_address = get_client_ip(self.request)
        logger.info(str(ip_address)+"-"+str(self.request))
        # return reverse('post-list')
        return reverse('blog:post-detail', kwargs={'pk': self.object.post.id})


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post-list')

    def get_queryset(self):
        ip_address = get_client_ip(self.request)
        logger.info(str(ip_address)+"-"+str(self.request))
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    # success_url = reverse_lazy('blog:post-list')

    def get_queryset(self):
        ip_address = get_client_ip(self.request)
        logger.info(str(ip_address)+"-"+str(self.request))
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

    def get_success_url(self):
        ip_address = get_client_ip(self.request)
        logger.info(str(ip_address)+"-"+str(self.request))
        # return reverse('post-list')
        return reverse('blog:post-detail', kwargs={'pk': self.object.post.id})

    # def form_valid(self, form):
    #     ip_address = get_client_ip(self.request)
    #     logger.info(str(ip_address)+"-"+str(self.request))
    #     author = self.request.user
    #     myform = form.save(commit=False)
    #     myform.author = author
    #     form.save()
    #     return super(PostCreateView, self).form_valid(form)
    # def get_context_data(self, **kwargs):
    #     ip_address = get_client_ip(self.request)
    #     logger.info(str(ip_address)+"-"+str(self.request))
    #     context = super(PostListView, self).get_context_data(**kwargs)
    #     return context

        # def get_form_kwargs(self, *args, **kwargs):
    #     ip_address = get_client_ip(self.request)
    #     logger.info(str(ip_address)+"-"+str(self.request))
    #     kwargs = super(PostCreateView, self).get_form_kwargs(*args, **kwargs)
    #     # kwargs['user'] = self.request.user
    #     return kwargs

    # def get_initial(self):
    #     ip_address = get_client_ip(self.request)
    #     logger.info(str(ip_address)+"-"+str(self.request))
    #     return {
    #         'author': self.request.user,
    #     }


# class CommentCreateView(LoginRequiredMixin, CreateView):
#     model = Comment
#     success_url = reverse_lazy('blog:post-list')
#     form_class=CommentForm
#     post_id=""
#     def get_initial(self):
#         ip_address = get_client_ip(self.request)
#         logger.info(str(ip_address)+"-"+str(self.request))
#         return {
#             'author':self.request.user,
#             'post':self.post_id
#         }
#     def get(self, request, *args, **kwargs):
#         self.post_id=self.kwargs['pk']
#         return super().get(request, *args, **kwargs)

#     def get_context_data(self, **kwargs):
#         ip_address = get_client_ip(self.request)
#         logger.info(str(ip_address)+"-"+str(self.request))
#         context=super().get_context_data(**kwargs)
#         context['post']=Post.objects.get(pk=self.post_id)
#         return context

    # def get_form_kwargs(self, *args, **kwargs):
    #     kwargs = super(CommentCreateView, self).get_form_kwargs(*args, **kwargs)
    #     kwargs['post'] = Post.objects.get(pk=self.post_id)
    #     return kwargs
        # def get_form_kwargs(self, *args, **kwargs):
    #     ip_address = get_client_ip(self.request)
    #     logger.info(str(ip_address)+"-"+str(self.request))
    #     kwargs = super(PostUpdateView, self).get_form_kwargs(*args, **kwargs)
    #     kwargs['user'] = self.request.user
    #     return kwargs
