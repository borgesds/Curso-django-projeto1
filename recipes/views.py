from django.shortcuts import render
from utils.recipes.factory import make_recipe
from recipes.models import Recipe


def home(request):
    # Vamos buscar todas as receitas em Admin pela ultima
    # is_published=True vai filtrar se foi o não publicado
    recipes = Recipe.objects.filter(
        is_published=True,
    ).order_by('-id')

    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
        # Aqui ja foi usado:cria uma lista de 10 receitas na home
        # Agora busca direto em Admin
    })
    # automaticamente busca pasta templates/...


def category(request, category_id):
    # Vamos filtrar as categorias
    """
    Estou pedindo minha Recipe para filtrar os objetos por categoria,
    mais pelo id dessa categoria como acesso o id dentro da categoria
    em Recipe?
    Uso __id=category_id.
    """
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True,
    ).order_by('-id')

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        # Aqui ja foi usado:cria uma lista de 10 receitas na home
        # Agora busca direto em Admin
    })
    # automaticamente busca pasta templates/...


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        # cria uma unica receita
        'is_detail_page': True,
    })
    # automaticamente busca pasta templates/...
