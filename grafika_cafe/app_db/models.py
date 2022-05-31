from sqlite3 import Timestamp
from tkinter import CASCADE
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class User (models.Model):
    id = models.BigAutoField(primary_key = True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    
    peran = [
        ('Kasir','Kasir'),
        ('Manager','Manager'),
        ('Admin','Admin')
    ]
    
    level = models.CharField(max_length=10, choices=peran, default='Kasir')
    
    class Meta:
        db_table = "user"
    
class Menu (models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length= 100, unique=True)
    harga = models.IntegerField()
    
    class Meta:
        db_table = "menu"

class Transaksi (models.Model):
    id = models.BigAutoField(primary_key=True)
    cashier = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "transaksi"
    
class List (models.Model):
    transaction = models.ForeignKey(Transaksi, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    qty = models.IntegerField(default = 1 ,validators=[
        MaxValueValidator(99),
        MinValueValidator(1)
    ])
    
    class Meta:
        db_table = "list"
    
class Aktivitas (models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length = 100)
    
    class Meta:
        db_table = "aktivitas"
    