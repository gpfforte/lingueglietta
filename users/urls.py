from django.urls import path, include, re_path

from . import views

urlpatterns = [
    # re_path(r'^$', views.home, name='home'),
    re_path(r'^signup/$', views.signup, name='signup'),
    #re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #      views.activate, name='activate'),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    
]