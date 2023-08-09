from django.contrib import admin

from cooking_almanach.recipes.models import RecipeModel


# Register your models here.

@admin.register(RecipeModel)
class AdministerRecipeModel(admin.ModelAdmin):
    pass

