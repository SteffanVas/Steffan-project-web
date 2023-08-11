from django.contrib.auth import models as auth_models
from django.contrib.auth.hashers import make_password
from django.db import models


class AlmanachContributorManager(auth_models.BaseUserManager):
    # overwrites auth_models.UserManager
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")

        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class AlmanachContributor(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):

    # overwriting auth_models.AbstractUser
    USERNAME_FIELD = 'email'
    objects = AlmanachContributorManager()
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
    )
    is_staff = models.BooleanField(
        default=False,
    )

