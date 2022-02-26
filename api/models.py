from django.db import models
from django.forms import CharField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class employee(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=8, unique=True)
    
    list = [
        ('Cashier', 'Cashier'),
        ('Supervisor', 'Supervisor'),
        ('Admin', 'Admin'),
    ]
    
    role = models.CharField(
        choices=list, 
        default='Cashier',
        max_length= 10
        )
    
    
    class Meta:
        db_table = 'employee'
class transaction(models.Model):
    id=models.BigAutoField(primary_key = True)
    operator=models.ForeignKey(employee , on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    table = models.IntegerField(validators =[
        MaxValueValidator(100),
        MinValueValidator(1)
    ])
    total = models.DecimalField(max_digits=6, decimal_places=2)
    
    class Meta:
        db_table = 'transaction'

class menu(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=40)
    code = models.CharField(max_length=8)
    price = models.DecimalField( max_digits=5, decimal_places=2)
    
    menu_status = [
        ('Unavailable', 'Unavailable'),
        ('Available', 'Available')
    ]
    
    status = models.CharField(choices=menu_status, max_length=12, default= 'Available')
    desc = models.TextField(blank=True)
    
    menu_type = [
        ('Beverages', 'Beverages'),
        ('Food', 'Food')
    ]
    
    type = models.CharField(choices=menu_type, max_length=10)
    
    class Meta:
        db_table = 'menu'

class detail(models.Model):
    transaction = models.ForeignKey(transaction, on_delete=models.CASCADE)
    food = models.ForeignKey(menu, on_delete=models.CASCADE)
    qty = models.IntegerField(default = 1 ,validators=[
        MaxValueValidator(99),
        MinValueValidator(1)
    ])
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    class Meta:
        db_table = 'detail'