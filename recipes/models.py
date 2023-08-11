from django.db import models
from django.template.defaultfilters import slugify

from cooking_almanach.accounts_auth.models import AlmanachContributor
from cooking_almanach.recipes.validators import time_too_long
from cooking_almanach.web.models import DataContrib

# from cooking_almanach.web.models import DataContrib


class RecipeModel(models.Model):
    recipe_title = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=1000)
    cooking_time = models.IntegerField(validators=(time_too_long,))
    servings = models.IntegerField()
    description = models.TextField()

    slug = models.SlugField(unique=True, null=False, blank=True, editable=False)
    type_of_meal = models.CharField(max_length=30,
                                    choices=(
                                        ('Vegetarian', 'Vegetarian'),
                                        ('Vegan', 'Vegan'),
                                        ('Gluten Free', 'Gluten Free'),
                                        ('Meat', 'Meat'),
                                        ('Other', 'Other'),
                                    ),

                                    )
    user = models.ForeignKey(to=AlmanachContributor, on_delete=models.CASCADE)
    user_unique_name = models.ForeignKey(to=DataContrib, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            super().save(*args, **kwargs)  # Save to get a primary key assigned
            self.slug = slugify(f'{self.recipe_title}-{self.pk}')  # Use the pk now
            super().save(*args, **kwargs)  # Save again with the updated slug
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.recipe_title}"


class Comment(models.Model):
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    poster = models.ForeignKey(to=AlmanachContributor, on_delete=models.CASCADE)
    poster_two = models.ForeignKey(to=DataContrib, on_delete=models.CASCADE)
