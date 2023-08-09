from django.contrib import admin
from django.urls import path, include

from cooking_almanach.recipes.views import CommentView, CreatingCommentView, recipe_index, edit_recipe, recipe_details, \
    all_recipes, all_personal_recipes, delete_recipe

# RecipeCreate,

urlpatterns = [
    path('form/', recipe_index, name='recipes'),
    path('<int:user_id>/<slug:recipe_title>/', include([
        path('edit/', edit_recipe, name='edit-recipe'),
        path('view/', recipe_details, name='view-recipe'),
        path('deleterecipe/', delete_recipe, name='delete-recipe')])),

    path('<int:user_id>/allmyrecipes', all_personal_recipes, name='list-of-my-recipes'),
    path('comment/', CreatingCommentView.as_view(), name='comment'),
    path('comments/', CommentView.as_view(), name='list-of-comments'),
    path('allrecipes/', all_recipes, name='list-of-recipes'),
]
# path('form/', RecipeCreate.as_view(), name='recipes'),
# path('comment/', add_comment, name='comment'),