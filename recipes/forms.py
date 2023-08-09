from django import forms

from cooking_almanach.recipes.models import RecipeModel, Comment


# , Comment


class RecipeForm (forms.ModelForm):
    class Meta:
        model = RecipeModel
        fields = '__all__'
        exclude = ['user', 'user_unique_name']
#
#
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['poster', 'poster_two']

