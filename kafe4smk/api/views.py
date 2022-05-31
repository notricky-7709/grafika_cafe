from rest_framework import viewsets
from rest_framework import permissions
from api.models import employee, transaction, menu, detail
from api.serializers import DetailSerializer, EmployeeSerializer,MenuSerializer,TransactionSerializer

# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class MenuViewSet(viewsets.ModelViewSet):
    queryset = menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]