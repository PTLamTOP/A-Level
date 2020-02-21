"""cinema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from profiles.api.views import CustomLoginView, CustomLogoutView, CustomRegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('filmsessions.urls', namespace='film-sessions')),
    path('halls/', include('halls.urls', namespace='halls')),
    path('tickets/', include('tickets.urls', namespace='tickets'))
]

urlpatterns += [
    path('rest-auth/registration/', CustomRegisterView.as_view(), name='rest_register'),
    path('rest-auth/login/', CustomLoginView.as_view(), name='rest_login'),
    path('rest-auth/logout/', CustomLogoutView.as_view(), name='rest_logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
