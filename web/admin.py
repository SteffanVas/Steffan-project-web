from django.contrib import admin

from cooking_almanach.web.models import TipModel, DataContrib


@admin.register(TipModel)
class TipModelAdmin(admin.ModelAdmin):
    pass


@admin.register(DataContrib)
class NamesUsernamesAdmin(admin.ModelAdmin):
    list_display = ('contributor_id', 'first_name', 'second_name', 'unique_username')