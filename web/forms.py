from django import forms

from cooking_almanach.web.models import TipModel


class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False)


class TipForm(forms.ModelForm):
    class Meta:
        model = TipModel
        fields = '__all__'