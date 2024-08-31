from django.shortcuts import render
from .models import Pais, Cliente


def pais_list(request):
    paises = Pais.objects.all()
    return render(request, 'clientes/pais_list.html', {'paises': paises})    