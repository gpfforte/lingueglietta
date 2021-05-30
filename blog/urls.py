
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    
    path('', views.PostListView.as_view(), name='post-list'),
    path('create/', views.PostCreateView.as_view(), name='post-create'),
    path('detail/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='post-update'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='post-delete'),
    
]
