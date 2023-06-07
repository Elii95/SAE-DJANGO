from django import forms
from .models import Machine, Infrastructure, Utilisateur


class AddMachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['nom', 'user', 'maintenanceDate', 'mach', 'ip', 'etat']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'maintenanceDate': forms.DateInput(attrs={'class': 'form-control'}),
            'mach': forms.Select(attrs={'class': 'form-control'}),
            'ip': forms.TextInput(attrs={'class': 'form-control'}),
            'etat': forms.Select(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = Utilisateur.objects.filter(role='employe')
        
class InfrastructureForm(forms.ModelForm):
    class Meta:
        model = Infrastructure
        fields = ['nom', 'responsable', 'machine', 'etage']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'responsable': forms.Select(attrs={'class': 'form-control'}),
            'machine': forms.Select(attrs={'class': 'form-control'}),
            'etage': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['responsable'].queryset = Utilisateur.objects.filter(role='responsable')

        
class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ('prenom', 'nom', 'email', 'role')
        widgets = {
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
        }
        
