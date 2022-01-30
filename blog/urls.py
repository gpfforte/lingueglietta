from django.urls import path, include
from . import views

app_name = 'blog'   


urlpatterns = [path('posts/', views.PostListView.as_view(), name='post-list'), ]
urlpatterns += [path('post/<int:pk>',
                     views.PostDetailView.as_view(), name='post-detail'), ]
urlpatterns += [path('post/create',
                     views.PostCreateView.as_view(), name='post-create'), ]
urlpatterns += [path('post/<int:pk>/update',
                     views.PostUpdateView.as_view(), name='post-update'), ]
urlpatterns += [path('post/<int:pk>/delete',
                     views.PostDeleteView.as_view(), name='post-delete'), ]
urlpatterns += [path('post/comment/<int:pk>/delete',
                     views.CommentDeleteView.as_view(), name='comment-delete'), ]
urlpatterns += [path('post/comment/<int:pk>/update',
                     views.CommentUpdateView.as_view(), name='comment-update'), ]