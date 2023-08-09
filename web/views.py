from django.contrib.auth import mixins as mixins_views
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from cooking_almanach.recipes.models import RecipeModel
from cooking_almanach.web.forms import SearchForm
from cooking_almanach.web.models import TipModel


class CreateTip(mixins_views.LoginRequiredMixin, mixins_views.UserPassesTestMixin, views.CreateView):
    model = TipModel
    template_name = 'web/tip-of-the-day.html'
    fields = '__all__'
    success_url = reverse_lazy('recipes')

    def test_func(self):
        return self.request.user.is_staff


class ViewTip (views.ListView):
    model = TipModel
    template_name = 'web/home_page.html'
    fields = '__all__'
    # latest_title = TipModel.objects.latest('title')
    # latest_tip = TipModel.objects.latest('tip')
    #     template_name = 'web/tip-of-the-day-customer-view.html'

class SearchView(views.FormView):
    template_name = 'web/search.html'
    form_class = SearchForm

    def form_valid(self, form):
        search_query = form.cleaned_data.get('search_query', '')
        search_results = RecipeModel.objects.filter(recipe_title__icontains=search_query)
        return render(self.request, self.template_name, {'form': form, 'search_results': search_results})