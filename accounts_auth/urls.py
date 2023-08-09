from django.contrib import admin
from django.urls import path, include
from cooking_almanach.accounts_auth.views import RegisterUserView, LoginContribView, LogoutContribView, ViewUser, \
    EditUser, EditUserEmail, UserDeleteView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='registration'),
    path('login/', LoginContribView.as_view(), name='login'),
    path('logout/', LogoutContribView.as_view(), name='logout'),
    path('<int:user_id>/view/', ViewUser.as_view(), name='view-edit'),
    path('<int:pk>/edit/', EditUser.as_view(), name='edit-profile-page'),
    path('<int:pk>/editemail/', EditUserEmail.as_view(), name='edit-email'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='delete-account')
]
