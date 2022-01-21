from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'info'    
urlpatterns = [    
    path('poesia/', views.poesia, name='poesia'),
    path('percorsi/', views.percorsi, name='percorsi'),
    path('cappelletta/', views.cappelletta, name='cappelletta'),
    path('san_rocco/', views.san_rocco, name='san_rocco'),
    path('san_pietro/', views.san_pietro, name='san_pietro'),
    path('about/', views.about, name='about')
]