from django.shortcuts import render, get_object_or_404, redirect
from .models import Machine, Infrastructure, Utilisateur
from .forms import AddMachineForm, InfrastructureForm, UtilisateurForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'templates/index.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('index')  # Redirect to the admin dashboard or any other admin-specific view
        else:
            error_message = "Invalid login credentials or unauthorized access"
            return render(request, 'ManagementApp/admin_login.html', {'error_message': error_message})
    else:
        return render(request, 'ManagementApp/admin_login.html')
    
def admin_logout(request):
    logout(request)
    return redirect('index')

@login_required
def machine_list(request):
    machines = Machine.objects.all()
    context = {'machines': machines}
    return render(request, 'machine/machine_list.html', context)

@login_required
def machine_detail(request, pk):
    machine = get_object_or_404(Machine, id=pk)
    context = {'machine': machine}
    return render(request, 'machine/machine_detail.html', context)

@login_required
def machine_add(request):
    if request.method == 'POST':
        form = AddMachineForm(request.POST or None)
        if form.is_valid():
            new_machine = Machine(nom=form.cleaned_data['nom'], user=form.cleaned_data['user'], maintenanceDate=form.cleaned_data['maintenanceDate'], mach=form.cleaned_data['mach'])
            new_machine.save()
            return redirect('machine_list')
    else:
        form = AddMachineForm()
    context = {'form': form}
    return render(request, 'machine/machine_add.html', context)

@login_required
def machine_delete(request, pk):
    machine = get_object_or_404(Machine, id=pk)
    if request.method == 'POST':
        machine.delete()
        return redirect('machine_list')
    context = {'machine': machine}
    return render(request, 'machine/confirm_delete.html', context)

@login_required
def infrastructure_list(request):
    infrastructures = Infrastructure.objects.all()  
    return render(request, 'infrastructure/infrastructure_list.html', {'infrastructures': infrastructures})

@login_required
def infrastructure_detail(request, pk):
    infrastructure = get_object_or_404(Infrastructure, id=pk)
    return render(request, 'infrastructure/infrastructure_detail.html', {'infrastructure': infrastructure})      

@login_required
def infrastructure_add(request):
    if request.method == 'POST':
        form = InfrastructureForm(request.POST)
        if form.is_valid():
            infrastructure = Infrastructure(nom=form.cleaned_data['nom'], responsable=form.cleaned_data['responsable'])
            infrastructure.save()
            return redirect('infrastructure_detail', pk=infrastructure.pk)
            
    else:
        form = InfrastructureForm()
    return render(request, 'infrastructure/infrastructure_add.html', {'form': form})

@login_required
def infrastructure_delete(request, pk):
    infrastructure = get_object_or_404(Infrastructure, id=pk)
    if request.method == 'POST':
        infrastructure.delete()
        return redirect('infrastructure_list')
    return render(request, 'infrastructure/confirm_delete.html', {'infrastructure': infrastructure})

@login_required
def utilisateur_list(request):
    utilisateurs = Utilisateur.objects.all()
    return render(request, 'utilisateur/list.html', {'utilisateurs': utilisateurs})

@login_required
def utilisateur_detail(request, pk):
    utilisateur = get_object_or_404(Utilisateur, id=pk)
    return render(request, 'utilisateur/detail.html', {'utilisateur': utilisateur})

@login_required
def utilisateur_create(request):
    if request.method == 'POST':
        form = UtilisateurForm(request.POST or None)
        if form.is_valid():
            utilisateur = Utilisateur(nom=form.cleaned_data['nom'], prenom=form.cleaned_data['prenom'], email=form.cleaned_data['email'], role=form.cleaned_data['role'])
            utilisateur.save()
            return redirect('utilisateur_detail', pk=utilisateur.pk )
    else:
        form = UtilisateurForm()
    return render(request, 'utilisateur/form.html', {'form': form})

@login_required
def utilisateur_update(request, pk):
    utilisateur = get_object_or_404(Utilisateur, id=pk)
    if request.method == 'POST':
        form = UtilisateurForm(request.POST, instance=utilisateur)
        if form.is_valid():
            utilisateur = Utilisateur(nom=form.cleaned_data['nom'], prenom=form.cleaned_data['prenom'], email=form.cleaned_data['email'], role=form.cleaned_data['role'])
            utilisateur.save()
            return redirect('utilisateur_detail', pk=utilisateur.pk)
    else:
        form = UtilisateurForm(instance=utilisateur)
    return render(request, 'utilisateur/form.html', {'form': form})

@login_required
def utilisateur_delete(request, pk):
    utilisateur = get_object_or_404(Utilisateur, id=pk)
    if request.method == 'POST':
        utilisateur.delete()
        return redirect('utilisateur_list')
    return render(request, 'utilisateur/confirm_delete.html', {'utilisateur': utilisateur})