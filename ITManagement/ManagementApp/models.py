from django.db import models
from datetime import datetime

class Utilisateur(models.Model):
    ROLE_CHOICES = (
        ('employe', 'Employé'),
        ('responsable', 'Responsable'),
    )
    id = models.AutoField(
        primary_key=True,
        editable=False
    )
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Machine(models.Model):
    TYPE= (
        ('PC', ('PC - Run Windows')),
        ('MAC', ('MAC - Run MacOS')),
        ('Serveur' , ('Serveur - Simple Server to deploy virtual machines')),
        ('Switch' , ('Switch - To maintains and connect servers')),
    )
    ETAT_CHOICES = (
        ('en ligne', ('en ligne')),
        ('hors ligne', ('hors ligne')),
    )
    id = models.AutoField(
        primary_key=True,
        editable=False
    )
    user = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, null=True, blank=True,limit_choices_to={'role': 'employe'})
    nom = models.CharField(max_length=20)
    maintenanceDate = models.DateField(default= datetime.now)
    mach = models.CharField(max_length=32, choices=TYPE, default='PC')
    ip = models.GenericIPAddressField(default='0.0.0.0')
    etat = models.CharField(max_length=20, choices=ETAT_CHOICES, default='en ligne')

    def __str__(self):
        return self.nom

class Infrastructure(models.Model):
    id = models.AutoField(
        primary_key=True,
        editable=False
    )

    nom = models.CharField(max_length=100)
    responsable = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, null=True, blank=True,limit_choices_to={'role': 'responsable'})
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    etage = models.IntegerField(default=0)

    def __str__(self):
        return self.nom