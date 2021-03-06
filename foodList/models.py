from django.db import models

class Recipe(models.Model):
    recipeName = models.CharField(max_length=50)
    recipeCalories = models.IntegerField(default=0)

    pork = models.BooleanField(default=False)
    alcohol = models.BooleanField(default=False)
    gluten = models.BooleanField(default=False)
    lactose = models.BooleanField(default=False)
    egg = models.BooleanField(default=False)
    meat = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    fish = models.BooleanField(default=False)
    containsMilk = models.BooleanField(default=False)
    containsMilkSubstitute = models.BooleanField(default=False)

    def __str__(self):
        return self.recipeName