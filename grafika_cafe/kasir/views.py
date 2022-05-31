from multiprocessing import context
from django.shortcuts import redirect, render
from app_db.models import *

# Create your views here.
def load_pemesanan(request):
    Menu = Menu.objects.all()
    context = {
        'Menu':Menu,
    }
    
    return render(request, "kasir-pesan.html", context)

def process_pemesanan(request):
    
    temp = Transaksi.objects.create(cashier = request.session['id'])
    temp.save()
    
    loop_id = Menu.objects.all()
    
    for x in loop_id :
        loop_temp =  request.POST.get('field'+x.get('id'))
        
        if(loop_temp != " " and loop_temp != ""):
            loop_save = List.objects.create(transaction = temp.get('id'), menu = x.get('id'), qty = int(loop_temp))
            loop_save.save()
            
    return redirect()

def load_list(request):
    
    lists = Transaksi.objects.filter(cashier = request.session['id']).order_by('timestamp')
    
    context = {
        'daftar' : lists,
    }
    
    return render(request, "kasir-list.html",context)