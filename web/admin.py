from django.contrib import admin

from cooking_almanach.web.models import TipModel


@admin.register(TipModel)
class TipModelAdmin(admin.ModelAdmin):
    pass
