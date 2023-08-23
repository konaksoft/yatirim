from django.urls import path

from apps.forms.views import *

app_name = 'forms'

urlpatterns = [
    path('add', add_form, name='add'),
    path('delete', delete_form, name='delete'),
]
