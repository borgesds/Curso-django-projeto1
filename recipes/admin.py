from django.contrib import admin
from .models import Category, Recipe

# Register your models here.


# Primeiro método de registrar no Admin
class CategoryAdmin(admin.ModelAdmin):
    ...


# Segundo método de registrar no Admin usando o decoration
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...


# Primeiro método de registrar no Admin
admin.site.register(Category, CategoryAdmin)
