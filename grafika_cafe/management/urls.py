from argparse import Namespace
from django.urls import path

from . import views

app_name = "management"
urlpatterns = [
    path('view/', views.load_menu, name='menu'),
    path('create/', views.create_menu, name = 'register'),
    path('edit/<int:menu_id>/', views.edit_menu, name = 'update'),
    path('delete/<int:menu_id>/', views.delete_menu, name = 'delete'),
    path('log/' , views.load_log, name='log'),
    path('list/', views.load_list, name='list')
]
