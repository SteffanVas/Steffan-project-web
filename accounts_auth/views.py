from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import views as auth_views
from django.contrib.auth import mixins as auth_mixins
from django.core.exceptions import PermissionDenied

# from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views

# from cooking_almanach.accounts_auth.models import AlmanachContributor
from cooking_almanach.web.models import DataContrib

# from django.views.generic import CreateView

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
    )
    second_name = forms.CharField(
        max_length=30,
        required=True,
    )

    unique_username = forms.CharField(max_length=20, )

    class Meta:
        model = UserModel
        fields = ('email',)

    def save(self, commit=True):
        user = super().save(commit)
        contributors = DataContrib(
            first_name=self.cleaned_data['first_name'],
            second_name=self.cleaned_data['second_name'],
            unique_username=self.cleaned_data['unique_username'],
            contributor_id=user.pk,
        )
        if commit:
            contributors.save()
        return user


class RegisterUserView(views.CreateView):
    template_name = 'accounts/registration-page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('home-page')

    # def form_valid(self, form):
    #     result = super().form_valid(form)
    #
    #     login(self.request, self.object)
    #     return result


class LoginContribView(auth_views.LoginView):
    template_name = 'accounts/login.html'


class LogoutContribView(auth_views.LogoutView):
    pass


class ViewUser(auth_mixins.LoginRequiredMixin, RegisterUserForm, views.ListView):
    model = UserModel
    template_name = 'accounts/user-profile-page.html'

    # class_form = RegisterUserForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['verification'] = UserModel.objects.get(pk=self.request.user.id)
        context['other_data'] = DataContrib.objects.get(pk=self.request.user.id)
        return context

    # def get_object(self, queryset=None):
    #     return get_object_or_404(UserModel, user=self.request.user)
    #
    # def test_func(self):
    #     user_profile = self.get_object()
    #     if self.request.user == user_profile.user:
    #         return True
    #     else:
    #         raise PermissionDenied('Authorization is denied')


class EditUser(auth_mixins.LoginRequiredMixin, auth_mixins.UserPassesTestMixin, views.UpdateView):
    template_name = 'accounts/user-profile-edit-page.html'
    model = DataContrib
    fields = ('first_name', 'second_name', 'unique_username')

    def get_success_url(self):
        return reverse_lazy('view-edit', kwargs={'user_id': self.object.pk})

    def get_object(self, queryset=None):
        user_profile = DataContrib.objects.get(contributor_id=self.request.user.id)
        return user_profile

    def test_func(self):
        user_profile = self.get_object()

        if self.request.user.id == user_profile.contributor.id:
            return True
        else:
            raise PermissionDenied('Authorization is denied')


class EditUserEmail(auth_mixins.LoginRequiredMixin, auth_mixins.UserPassesTestMixin, views.UpdateView):
    template_name = 'accounts/change-email.html'
    model = UserModel
    fields = ('email',)

    # success_url = reverse_lazy('view-edit')
    def get_success_url(self):
        return reverse_lazy('view-edit', kwargs={'user_id': self.object.pk})

    def get_object(self, queryset=None):
        user_profile = UserModel.objects.get(id=self.request.user.id)
        return user_profile

    def test_func(self):
        user_profile = self.get_object()

        if self.request.user.id == user_profile.id:
            return True
        else:
            raise PermissionDenied('Authorization is denied')


class UserDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = UserModel
    template_name = 'accounts/contrib_confirm_delete.html'
    success_url = reverse_lazy('home-page')

    # needs polishing
    # def get_object(self, queryset=None):
    #     return get_object_or_404(UserModel, pk=self.request.user.id)
    #
    # def test_func(self):
    #     user_profile_id = self.get_object()
    #
    #     if self.request.user.id == user_profile_id:
    #         return True
    #     else:
    #         raise PermissionDenied('Authorization is denied')


# class ManagePermissions:
#     user = AlmanachContributor.objects.filter(is_staff='admin')
#     user.has_perm('main_app.add_employee')  # True
#     user.has_perm('main_app.change_employee')  # True
#     user.has_perm('main_app.delete_employee')  # True
#     user.has_perm('main_app.view_employee')

