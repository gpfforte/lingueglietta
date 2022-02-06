"""gpfblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from . import views
app_name = 'blog'


urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post-list'), ]
urlpatterns += [
    path('myposts/<str:mine>', views.PostListView.as_view(), name='my-post-list'), ]
urlpatterns += [path('post/<int:pk>',
                     views.PostDetailView.as_view(), name='post-detail'), ]
urlpatterns += [path('post/create',
                     views.PostCreateView.as_view(), name='post-create'), ]
urlpatterns += [path('post/<int:pk>/update',
                     views.PostUpdateView.as_view(), name='post-update'), ]
urlpatterns += [path('post/<int:pk>/delete',
                     views.PostDeleteView.as_view(), name='post-delete'), ]
# urlpatterns += [path('post/<int:pk>/comment', views.CommentCreateView.as_view(), name='post-comment'),]
urlpatterns += [path('post/comment/<int:pk>/delete',
                     views.CommentDeleteView.as_view(), name='comment-delete'), ]
urlpatterns += [path('post/comment/<int:pk>/update',
                     views.CommentUpdateView.as_view(), name='comment-update'), ]
