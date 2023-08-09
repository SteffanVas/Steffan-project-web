from django.contrib import admin
from django.urls import path, include

from cooking_almanach.web.views import CreateTip, ViewTip, SearchView

urlpatterns =[
    path('', ViewTip.as_view(), name='home-page'),
    path('tip/', CreateTip.as_view(), name='tip-of-the-day'),
    path('search/', SearchView.as_view(), name='search')

]