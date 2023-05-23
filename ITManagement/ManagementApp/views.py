from django.shortcuts import render, get_object_or_404, redirect
from .models import Machine, Infrastructure, User
from .forms import AddMachineForm, InfrastructureForm

def home(request):
    return render(request, 'templates/index.html')

def machine_list(request):
    machines = Machine.objects.all()
    context = {'machines': machines}
    return render(request, 'ManagementApp/machine_list.html', context)

def machine_detail(request, pk):
    machine = get_object_or_404(Machine, id=pk)
    context = {'machine': machine}
    return render(request, 'ManagementApp/machine_detail.html', context)

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
    return render(request, 'ManagementApp/machine_add.html', context)

def machine_delete(request, pk):
    machine = get_object_or_404(Machine, id=pk)
    machine.delete()
    return redirect('machine_list')

def infrastructure_list(request):
    infrastructures = Infrastructure.objects.all()
    return render(request, 'ManagementApp/infrastructure_list.html', {'infrastructures': infrastructures})

def infrastructure_detail(request, pk):
    infrastructure = get_object_or_404(Infrastructure, pk=pk)
    return render(request, 'ManagementApp/infrastructure_detail.html', {'infrastructure': infrastructure})

def infrastructure_add(request):
    if request.method == 'POST':
        form = InfrastructureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('infrastructure_list')
    else:
        form = InfrastructureForm()
    return render(request, 'ManagementApp/infrastructure_add.html', {'form': form})


def infrastructure_delete(request, pk):
    infrastructure = get_object_or_404(Infrastructure, pk=pk)
    infrastructure.delete()
    return redirect('infrastructure_list')
