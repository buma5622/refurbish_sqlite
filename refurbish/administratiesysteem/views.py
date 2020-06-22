from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import RegistratieForm, ReparatieForm
from .models import Computer


def computers(request):
    context = {'computers': Computer.objects.all()}

    return render(request, 'computers.html', context)


def filter_data(request):
    processor = request.GET.get('processor')

    if processor:
        computers = Computer.objects.filter(processor__icontains=processor).values()

    else:
        computers = Computer.objects.all().values()

    return JsonResponse(list(computers), safe=False)


def computer_detail(request, id):
    context = {'computer': Computer.objects.get(id=id)}

    return render(request, 'computer_detail.html', context)


def registratie(request):
    return render(request, 'registratie.html')


def post_registratie(request):
    if request.method == 'POST':
        registratie_form = RegistratieForm(request.POST, request.FILES)
        if registratie_form.is_valid():
            registratie_form.save()
    else:
        reserve_form = RegistratieForm()

    return redirect('computers')


def reparatie(request):
    context = {'computers': Computer.objects.all()}

    return render(request, 'reparatie.html', context)


def reparatie_detail(request, id):
    context = {'computer': Computer.objects.get(id=id)}

    return render(request, 'reparatie_detail.html', context)


def post_reparatie(request, id):
    computer = Computer.objects.get(id=id)

    if request.method == 'POST':
        reparatie_form = ReparatieForm(request.POST,
                            request.FILES, instance=computer)

        if reparatie_form.is_valid():
            reparatie_form.save()
    else:
        reserve_form = RegistratieForm()

    return redirect('reparatie')
