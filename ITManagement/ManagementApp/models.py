from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Machine(models.Model):
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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=6)
    maintenanceDate = models.DateField(default= datetime.now)
    mach = models.CharField(max_length=32, choices=TYPE, default='PC')
    def __str__(self):
        return self.nom

class Infrastructure(models.Model):
    id = models.AutoField(
        primary_key=True,
        editable=False
    )
    nom = models.CharField(max_length=100)
    responsible = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Update(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Update for {self.machine.nom} by {self.updated_by.username}"
