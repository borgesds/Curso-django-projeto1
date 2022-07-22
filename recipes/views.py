from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html')

def contato(request):
    return HttpResponse('CONTATO 1')

def sobre(request):
    return HttpResponse('SOBRE 1')
