from django.contrib.auth.decorators import login_required
from django.contrib.auth import mixins as auth_mixins
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from django.views import generic as views
from django.core.paginator import Paginator

from cooking_almanach.accounts_auth.models import AlmanachContributor
from cooking_almanach.recipes.forms import RecipeForm, CommentForm
# , CommentForm
from cooking_almanach.recipes.models import Comment, RecipeModel \
    # , RecipeModel
from cooking_almanach.web.models import DataContrib


# from cooking_almanach.web.models import DataContrib


# from cooking_almanach.web.models import DataContrib


# class RecipeCreate (auth_mixins.LoginRequiredMixin,views.CreateView):
#     template_name = 'recipes/recipe_form.html'
#     model = RecipeModel
#     fields = "__all__"
#     success_url = reverse_lazy('recipes')


@login_required
def recipe_index(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.user_unique_name = DataContrib.objects.get(contributor_id=request.user.id)
            recipe.save()
            return redirect('view-recipe', recipe.user_id, recipe.slug)
    else:
        form = RecipeForm()

    context = {
        'form': form
    }

    return render(request, "recipes/recipe_form.html", context)


@login_required
def edit_recipe(request, user_id, recipe_title):
    recipe = RecipeModel.objects.get(slug=recipe_title)
    if request.user.id != recipe.user_id:
        raise Http404
    else:

        if request.method == "GET":
            form = RecipeForm(instance=recipe,
                              )
        else:
            form = RecipeForm(request.POST, instance=recipe)
            if form.is_valid():
                form.save()
                new_recipe_title = form.cleaned_data['recipe_title']
                recipe.slug = slugify(f'{new_recipe_title}-{recipe.id}')
                form.save()
                return redirect('view-recipe', user_id, recipe.slug)
        context = {'form': form}

        return render(request, 'recipes/recipe_form_edit.html', context)


@login_required
def delete_recipe(request, user_id, recipe_title):
    recipe = RecipeModel.objects.get(slug=recipe_title)
    if request.user.id != recipe.user_id:
        raise Http404
    else:

        if request.method == "GET":
            form = RecipeForm(instance=recipe, )
            context = {'form': form, 'recipe_title':  recipe_title}
            return render(request, 'recipes/delete-recipe.html', context)

        elif request.method == "POST":
            recipe.delete()
            return redirect('home-page')


def recipe_details(request, user_id, recipe_title):
    recipe = RecipeModel.objects.get(slug=recipe_title)
    context = {
        'recipe': recipe
    }

    return render(request, 'recipes/recipe_details.html', context)


def all_recipes(request):
    all_the_recipes = RecipeModel.objects.all()
    # paginator = Paginator(all_the_recipes, 5)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    context = {
        'all_recipes': all_the_recipes,
        # 'pages': page_obj,

    }
    return render(request, 'recipes/recipes_list.html', context)


def all_personal_recipes(request, user_id):
    my_recipes = RecipeModel.objects.filter(user_id=user_id)
    context = {
        'my_recipes': my_recipes
    }
    return render(request, 'recipes/recipes_list_personal.html', context)


# @login_required
# def add_comment(request):
#     if request.method == 'POST':
#         # photo = Photo.objects.get(id=photo_id)
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             # comment.to_photo = photo
#             comment.poster = request.user
#             comment.save()
#     else:
#         form = CommentForm()
#         return render(request, 'recipes', context=form)


class CreatingCommentView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = Comment
    template_name = 'recipes/comment_form.html'
    form_class = CommentForm
    success_url = reverse_lazy('recipes')

    def form_valid(self, form):
        almanach_contributor = get_object_or_404(AlmanachContributor, id=self.request.user.id)
        form.instance.poster = almanach_contributor
        data_contrib = get_object_or_404(DataContrib, contributor_id=self.request.user.id)
        form.instance.poster_two = data_contrib

        return super().form_valid(form)



class CommentView(views.ListView):
    model = Comment
    template_name = 'recipes/comments_list.html'

# class CommentView(views.TemplateView):
#     template_name = 'recipes/comments_list.html'
#     extra_context = {
#         'comments': Comment.objects.all(),
#     }

# class UserView (views.TemplateView):
#     template_name = 'recipes/comments_list.html'
#     extra_context = {
#         'users': DataContrib.objects.all(),
#     }
