from argparse import Namespace
from django.urls import path

from . import views

app_name = "gateway"
urlpatterns = [
    path('', views.get_login, name='login'),
    path('auth/', views.auth_login, name = 'auth'),
]
