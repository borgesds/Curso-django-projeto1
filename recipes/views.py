from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html')
    # automaticamente busca pasta templates/...


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html')
    # automaticamente busca pasta templates/...