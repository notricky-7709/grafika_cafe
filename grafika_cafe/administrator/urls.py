from argparse import Namespace
from django.urls import path

from . import views

app_name = "administrator"
urlpatterns = [
    path('view/', views.load_user, name='user'),
    path('create/', views.create_user, name = 'register'),
    path('edit/<int:user_id>/', views.edit_user, name = 'update'),
    path('delete/<int:user_id>/', views.delete_user, name = 'delete'),
    path('log/' , views.load_log, name='log')
]
