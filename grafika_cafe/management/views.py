from django import http
from django.shortcuts import redirect, render
from app_db.models import *
from django.http import HttpResponseRedirect

# Create your views here.
def load_menu(request):
    menus = Menu.objects.all()
    context = {
        'menu':menus,
    }
    
    return render(request, 'management-menu.html', context)

def create_menu(request):
    name = request.POST.get('name')
    price = request.POST.get('price')
    
    temp = Menu.objects.create(name = name, price = price)
    temp.save()
    
    return redirect('management:menu')
    
def edit_menu(request, menu_id):
    name = request.POST.get('name')
    price = request.POST.get('price')
    
    Menu.objects.filter(id = menu_id).update(name = name, price = price)
    
    return redirect('management:menu')
    
def delete_menu(request, menu_id):
    
    Menu.objects.filter(id = menu_id).delete()
    
    return redirect('management:menu')

def load_log(request):
    
    lists = Aktivitas.objects.all().order_by('timestamp')
    
    context = {
        'lists' : lists,
    }
    
    return render(request, "manager-log.html", context)

def load_list(request):
    
    lists = Transaksi.objects.all().order_by('timestamp')
    
    context = {
        'daftar' : lists,
    }
    return render(request, "manager-list.html", context)