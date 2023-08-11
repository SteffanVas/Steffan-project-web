from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group

UserModel = get_user_model()


class GroupMembershipInline(admin.StackedInline):
    model = Group.user_set.through  # This accesses the intermediate model for group membership
    extra = 1


@admin.register(UserModel)
class ContribModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'last_login', 'is_staff')
    list_filter = ('id', 'is_staff', 'last_login', 'email')
    search_fields = ('is_staff', 'email')
    sortable_by = ('id', 'last_login', 'email',)
    fieldsets = (('Registration Info', {'fields': ('email', 'last_login')}),
                 ('Website Role Info', {'fields': ('is_staff',)})
                 )





class CustomGroupAdmin(GroupAdmin):
    inlines = [GroupMembershipInline]


admin.site.unregister(Group)
admin.site.register(Group, CustomGroupAdmin)
