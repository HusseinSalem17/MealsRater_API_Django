from django.db import models

class Meal(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=360)
    
    def __str__(self):
        return self.name
    
class Rating(models.Model):
    meal=models.ForeignKey(Meal, on_delete=models.CASCADE)
    user