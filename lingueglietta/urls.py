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
from blog import views as blog_views
from django.conf.urls.static import static
from django.conf import settings
from users import views as users_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.index, name='index'),
    path('poesia/', blog_views.poesia, name='poesia'),
    path('percorsi/', blog_views.percorsi, name='percorsi'),
    path('about/', blog_views.about, name='about'),
]

urlpatterns += [
    path('blog/', include('blog.urls')),
]

urlpatterns += [
    path('users/', include('users.urls')),
]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Add Django site authentication urls (for login, logout, password management)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += [
    path('password/', users_view.change_password, name='change_password'),
]

