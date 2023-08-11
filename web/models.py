from django.contrib.auth import get_user_model
from django.db import models

# from cooking_almanach.accounts_auth.views import RegisterUserForm

UserModel = get_user_model()


class DataContrib(models.Model):
    first_name = models.CharField(
        max_length=30,
        # required=True,
    )
    second_name = models.CharField(
        max_length=30,
        # required=True,
    )

    unique_username = models.CharField(max_length=20, )

    # contributor = models.ForeignKey(to=UserModel,
    #                                 on_delete=models.CASCADE)

    contributor = models.OneToOneField(UserModel,
                                       on_delete=models.CASCADE,
                                       primary_key=True)

    def __str__(self):
        return f"{self.first_name} {self.second_name} with username {self.unique_username} "


class TipModel(models.Model):
    title = models.CharField()
    tip = models.TextField()

    def __str__(self):
        return f"{self.title}"

