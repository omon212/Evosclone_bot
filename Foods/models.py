from django.db import models


class FoodModel(models.Model):
    name_food = models.CharField(max_length=255, unique=True, null=False)
    price = models.ImageField()

    def __str__(self):
        return self.name_food

# Create your models here.
