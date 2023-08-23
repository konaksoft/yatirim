from django.urls import path
from apps.theme.views import *


app_name = 'theme'

urlpatterns = [
    path('', index_view, name=''),

]
