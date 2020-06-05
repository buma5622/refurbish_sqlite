from django.shortcuts import render, redirect
from .forms import RegistratieForm
from .models import Computer


def computers(request):
    context = {'computers': Computer.objects.all()}

    return render(request, 'computers.html', context)


def registratie(request):
    return render(request, 'registratie.html')


def post_registratie(request):
    if request.method == 'POST':
        registratie_form = RegistratieForm(request.POST)
        if registratie_form.is_valid():
            registratie_form.save()

    else:
        reserve_form = RegistratieForm()

    return redirect('computers')