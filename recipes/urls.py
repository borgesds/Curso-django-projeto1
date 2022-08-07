from django.urls import path

from . import views

"""
Está buscando o def home, contato,
sobre dentro da pasta recipes que tem o arquivo home

from recipes.views import home

"""

"""
Quando começa a importar vários módulos (home, sobre e etc),
fica muito grande a area de importação. Ex:

from recipes.views import home, views, sobre, contato

Então o melhor método é importar o modulo inteiro:

from . import views

O . significa da pasta onde você esta, import tudo que esta em views.py
"""

app_name = 'recipes'

urlpatterns = [
    # Home
    path('', views.home, name="home"),
    # Pegar a categoria das receitas
    path(
        'recipes/category/<int:category_id>/', views.category, name="category"
        ),
    # recipe
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]
