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

urlpatterns = [
    # Home
    path('', views.home),
    # recipe
    path('recipes/<int:id>/', views.recipe)
]
