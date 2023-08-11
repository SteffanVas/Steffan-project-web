from django.core.validators import ValidationError


def time_too_long(minutes_cooking):
    if minutes_cooking > 999:
        raise ValidationError("A meal can not take that long")
