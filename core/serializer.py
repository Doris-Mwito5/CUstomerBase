from rest_framework import serializers
from .models import Customer,Profession,Datasheet,Document

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'address', 'professions', 'datasheet', 'active']

class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ['id', 'description']        

class DatasheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datasheet
        fields = ['id', 'description', 'historical_data'] 
        
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'dtype', 'doc_number', 'customer']                 