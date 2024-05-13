from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from .models import Customer, Profession, Datasheet, Document
from rest_framework import viewsets
from .serializer import CustomerSerializer, ProfessionSerializer, DatasheetSerializer, DocumentSerializer 

class CustomerViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        active_customers = Customer.objects.filter(active=True)
        return active_customers
    
    
    def list(self, request, *args, **kwargs):
        import pdb; pdb.set_trace()
        customers = Customer.objects.filter(id=3)
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
        
    
class ProfessionViewset(viewsets.ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer   

class DatasheetViewset(viewsets.ModelViewSet):
    queryset = Datasheet.objects.all()
    serializer_class = DatasheetSerializer
    
class DocumentViewset(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer    