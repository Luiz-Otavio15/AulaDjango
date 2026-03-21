from django.shortcuts import render
from .models import *

def lista_filme(request):
    filmes = Filme.objects.all()
    return render(request, 'filmes/TelaInicial.html', {'filmes': filmes})