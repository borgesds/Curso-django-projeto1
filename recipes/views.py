from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html') #automaticamente busca pasta templates/...

def contato(request):
    return render(request, 'recipes/contato.html') #automaticamente busca pasta templates/...

def sobre(request):
    return HttpResponse('SOBRE 1')
