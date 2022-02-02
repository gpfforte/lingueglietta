"""lingueglietta URL Configuration

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
from django.contrib import admin
from django.urls import path, include
# from blog import views as blog_views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from . import views

urlpatterns = [path('', views.index, name='index'),]

urlpatterns += [
    path('nimda_gpf/', admin.site.urls),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
]

urlpatterns += [
    path('blog/', include('blog.urls')),
]

urlpatterns += [
    path('info/', include('info.urls')),
]

urlpatterns += [
    path('users/', include('users.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Add Django site authentication urls (for login, logout, password management)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

# urlpatterns += [
#     path('password/', users_view.change_password, name='change_password'),
# ]
