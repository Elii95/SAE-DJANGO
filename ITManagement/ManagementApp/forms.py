from django import forms
from django.contrib.auth.models import User
from .models import Machine, Infrastructure

class AddMachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['nom', 'user', 'maintenanceDate', 'mach']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'maintenanceDate': forms.DateInput(attrs={'class': 'form-control'}),
            'mach': forms.Select(attrs={'class': 'form-control'}),
        }

        def clean_name(self):
            name = self.cleaned_data['nom']
            if len(name) < 6:
                raise forms.ValidationError("Name must be at least 6 characters long")
            return name
        
class InfrastructureForm(forms.ModelForm):
    class Meta:
        model = Infrastructure
        fields = ['nom', 'responsible']
        widgets = {
            'responsible': forms.Select(attrs={'class': 'form-control'})
        }

        
