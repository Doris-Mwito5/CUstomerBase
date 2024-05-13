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
    
    # a custom action method that handles HTTP GET requests to list all customers
    def list(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace()
        customers = Customer.objects.filter(id=3)
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, *args, **kwargs):
        customer = self.get_object()  # Retrieve the specific customer instance
        # customers = self.get_object()
        if customer.active:  # Check if the customer is active
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        else:
            return Response({"detail": "Customer not found or inactive"}, status=404)
        
    # def create(self, request, *args, **kwargs):
    #     data = request.data
    #     Customer = Customer.objects.create(
    #         name=data['name'], address=data['address'], datasheet_id=data['datasheet']
    #     )    
    # profession = Profession.objects.get(id=data['profession'])
    # Customer.professions.add(profession)
    # Customer.save()
    
    # serializer = CustomerSerializer(Customer)
    # return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        data = request.data
                   # Create Customer object
        customer = Customer.objects.create(
            
            name=data['name'],
            address=data['address'],
            datasheet_id=data['datasheet']
            )
        profession = Profession.objects.get(id=data['profession'])
            # Add profession to Customer
        customer.professions.add(profession)
        customer.save()

            # Serialize Customer object
        serializer = CustomerSerializer(customer)

            # Return serialized data in response
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