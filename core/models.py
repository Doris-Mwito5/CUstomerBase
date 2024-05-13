from django.db import models

class Profession(models.Model):
    description = models.CharField(max_length=50)
    
class Datasheet(models.Model):
    description = models.CharField(max_length=50)
    historical_data = models.TextField()
    
    def __str__(self):
        return self.description
    
class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    professions = models.ManyToManyField(Profession)
    datasheet = models.OneToOneField(Datasheet, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
        
    def __str__(self):
        return self.name
    
class Document(models.Model):
    PP = 'PP'
    ID = 'ID'
    OT = 'OT'
    
    DOC_TYPE = (
    (PP, 'Passport'),
    (ID, 'Identity Card'),
    (OT, 'Others')
    )
    dtype = models.CharField(choices=DOC_TYPE, max_length=2)
    doc_number = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.doc_number



