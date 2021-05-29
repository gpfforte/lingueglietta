
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    
    path('', views.PostList.as_view(), name='blog-home'),
    path('create/', views.PostCreate.as_view(), name='post-create'),
    path('detail/<int:pk>', views.PostDetail.as_view(), name='post-detail'),
    
]
