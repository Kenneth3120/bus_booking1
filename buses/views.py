from django.shortcuts import render, redirect
from .forms import BusForm
from .models import Bus

def upload_bus(request):
    if request.method == 'POST':
        form = BusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_buses')
    else:
        form = BusForm()
    return render(request, 'buses/upload_bus.html', {'form': form})

def list_buses(request):
    buses = Bus.objects.all()
    return render(request, 'buses/list_buses.html', {'buses': buses})
    