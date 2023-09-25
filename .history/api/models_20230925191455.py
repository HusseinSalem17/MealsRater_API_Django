from django.db import models

class Meal(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max)
    
    def __str__(self):
        return self.name