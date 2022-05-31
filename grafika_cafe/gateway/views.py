from django.shortcuts import redirect, render
from app_db.models import *

# Create your views here.
def get_login(request):
    
    return render(request, "login.html")

def auth_login(request):
    temp_username = request.POST.get('username')
    temp_password = request.POST.get('password')
    
    temp = User.objects.filter(username = temp_username, password = temp_password)
    
    if(temp.exists() and temp.count() == 1):
        request.session['id'] = temp.get('id')
        
        if(temp.get('level') == "Admin"):
            return redirect("administrator:user")
        
        if(temp.get('level') == "Kasir"):
            return redirect("kasir:")
        
        if(temp.get('level') == "Manager"):
            return redirect("management:menu")