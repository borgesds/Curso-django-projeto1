from django.urls import path

"""
Esta buscando o def home, contato,
sobre dentro da pasta recipes que tem o arquivo home
"""
from recipes.views import home

urlpatterns = [
    # Home
    path('', home),
]
