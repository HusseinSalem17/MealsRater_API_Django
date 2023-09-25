from django.db import models

class Meal(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=360)
    
    def __str__(self):
        return self.name
    
class Rating(models.Model):
    meal=models.ForeignKey(Meal, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    stars=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])