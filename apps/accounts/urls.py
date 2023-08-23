from django.urls import path

from apps.accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('profile', profile_view, name='profile'),

]
