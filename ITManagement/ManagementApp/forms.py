from django import forms
from .models import Machine, Infrastructure, Utilisateur


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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = Utilisateur.objects.filter(role='employe')
        
class InfrastructureForm(forms.ModelForm):
    class Meta:
        model = Infrastructure
        fields = ['nom', 'responsable']
        widgets = {
            'responsable': forms.Select(attrs={'class': 'form-control'})
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['responsable'].queryset = Utilisateur.objects.filter(role='responsable')

        
class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ('prenom', 'nom', 'email', 'role')
