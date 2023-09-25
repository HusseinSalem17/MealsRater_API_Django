from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    rating = models.IntegerField()
    image = models.ImageField(upload_to="meal_images/", null=True, blank=True)

    def __str__(self):
        return self.name