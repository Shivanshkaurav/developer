from django.db import models
from django.conf import settings

from learn.storage_backends import PublicMediaStorage


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100, blank=False, null=False)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(storage=PublicMediaStorage() ,upload_to= 'images/')

    def __str__(self):
        return self.recipe_name