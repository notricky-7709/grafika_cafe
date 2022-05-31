from dataclasses import field, fields
from api.models import employee, menu, transaction,detail
from rest_framework import serializers

class EmployeeSerializer (serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = ['id','name','code','role']
        
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields = ['id','name','code','price','status','desc','type']
       
class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = detail
        fields = ['transaction', 'food', 'qty', 'price']

class TransactionSerializer(serializers.ModelSerializer):
    detail = DetailSerializer(many = True)
    class Meta:
        model = transaction
        fields = ['id','operator','date','table','detail','total']
    
    def create(self, data):
        detail_data =data.pop('detail')
        Detail = transaction.objects.create(**data)
        for data in detail_data:
            detail.objects.create(Detail = Detail, **data)
        return Detail