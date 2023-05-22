from django.db import models
from datetime import datetime

# Create your models here.

class Machine(models.Model) : 

    TYPE= (
        ('PC', ('PC - Run Windows')),
        ('MAC', ('MAC - Run MacOS')),
        ('Serveur' , ('Serveur - Simple Server to deploy virtual machines')),
        ('Switch' , ('Switch - To maintains and connect servers')),
    )
    id = models.AutoField(
        primary_key=True,
        editable=False
    )
    nom = models.CharField(max_length=6)
    maintenanceDate = models.DateField(default= datetime.now)
    mach = models.CharField(max_length=32, choices=TYPE, default='PC')
