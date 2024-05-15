from urllib import response
from django.shortcuts import render, Http404
from rest_framework.response import Response
from .models import Customer, Profession, Datasheet, Document
from rest_framework import viewsets
from .serializer import CustomerSerializer, ProfessionSerializer, DatasheetSerializer, DocumentSerializer 

class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    def get_queryset(self):
        active_customers = Customer.objects.filter(active=True)
        return active_customers
    
    def list(self, request, *args, **kwargs):
        customers = Customer.objects.filter(id=3)
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, *args, **kwargs):
        customer = self.get_object()  
        if customer.active: 
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        else:
            return Response({"detail": "Customer not found or inactive"}, status=404)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        customer = Customer.objects.create(
            
            name=data['name'],
            address=data['address'],
            datasheet_id=data['datasheet']
            )
        profession = Profession.objects.get(id=data['profession'])
        
        customer.professions.add(profession)
        customer.save()
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def update(self, request, pk=None):
        customer = self.get_object()  
        data = request.data
        customer.name = data.get('name', customer.name)
        customer.address = data.get('address', customer.address)
        customer.datasheet_id = data.get('datasheet', customer.datasheet_id)

        profession = Profession.objects.get(id=data['profession'])
        for p in customer.professions.all():
              customer.professions.remove(p)
              
        customer.professions.add(profession)      
        
        customer.save()

        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        customer = self.get_object()  
        data = request.data
        customer.name = data.get('name', customer.name)
        customer.address = data.get('address', customer.address)
        customer.datasheet_id = data.get('datasheet', customer.datasheet_id)
        customer.save()

        serializer = CustomerSerializer(customer)
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