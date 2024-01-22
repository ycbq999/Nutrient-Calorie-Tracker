from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Food(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    carbs = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    calories = models.FloatField()


class Consume(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)

 




