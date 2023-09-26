from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Meal(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=360)

    def no_of_ratings(self):
        ratings = Rating.objects.filter(meal=self)
        return len(ratings)

    # sum of ratings / number of ratings
    def avg_rating(self):
        ratings = Rating.objects.filter(meal=self)
        if len(ratings) > 0:
            return sum(rating.stars for rating in ratings) / len(ratings)
        return 0

    def __str__(self):
        return self.title


class Rating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.meal.title

    class Meta:
        unique_together = (("user", "meal"),)  # the user can only rate a meal once
        index_together = (("user", "meal"),)  # to improve the performance of queries
