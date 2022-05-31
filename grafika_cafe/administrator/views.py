from django import http
from django.shortcuts import redirect, render
from app_db.models import *
from django.http import HttpResponseRedirect

# Create your views here.
def load_user(request):
    users = User.objects.all()
    context = {
        'user':users,
    }
    
    return render(request, 'admin-home.html', context)

def create_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    level = request.POST['level']
    
    temp = User.objects.create(username = username, password = password, level = level)
    temp.save()
    
    return redirect('administrator:user')
    
def edit_user(request, user_id):
    username = request.POST.get('username')
    password = request.POST.get('password')
    level = request.POST['level']
    
    User.objects.filter(id = user_id).update(username = username, password = password, level = level)
    
    return redirect('administrator:user')
    
def delete_user(request, user_id):
    
    User.objects.filter(id = user_id).delete()
    
    return redirect('administrator:user')

def load_log(request):
    
    lists = Aktivitas.objects.all().order_by('timestamp')
    
    context = {
        'lists' : lists,
    }
    
    return render(request, "admin-log.html", context)