# Generated by Django 4.2.1 on 2023-05-23 23:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=6)),
                ('maintenanceDate', models.DateField(default=datetime.datetime.now)),
                ('mach', models.CharField(choices=[('PC', 'PC - Run Windows'), ('MAC', 'MAC - Run MacOS'), ('Serveur', 'Serveur - Simple Server to deploy virtual machines'), ('Switch', 'Switch - To maintains and connect servers')], default='PC', max_length=32)),
                ('ip', models.GenericIPAddressField(default='0.0.0.0')),
                ('etat', models.CharField(choices=[('en ligne', 'en ligne'), ('hors ligne', 'hors ligne')], default='en ligne', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(choices=[('employe', 'Employé'), ('responsable', 'Responsable')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ManagementApp.machine')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ManagementApp.utilisateur')),
            ],
        ),
        migrations.AddField(
            model_name='machine',
            name='user',
            field=models.OneToOneField(blank=True, limit_choices_to={'role': 'employe'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='ManagementApp.utilisateur'),
        ),
        migrations.CreateModel(
            name='Infrastructure',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('etage', models.IntegerField(default=0)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ManagementApp.machine')),
                ('responsable', models.OneToOneField(blank=True, limit_choices_to={'role': 'responsable'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='ManagementApp.utilisateur')),
            ],
        ),
    ]
