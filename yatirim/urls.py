"""
URL configuration for yatirim project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from apps.dashboard.views import dashboard_view
from apps.accounts.views import login_view, logout_view
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  include('apps.theme.urls'), name=''),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    # Dashboard
    path('dashboard', dashboard_view, name='dashboard'),
    # Accounts
    path('accounts',  include('apps.accounts.urls'), name='accounts'),
    # Forms
    path('forms/', include('apps.forms.urls'), name='forms')

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)