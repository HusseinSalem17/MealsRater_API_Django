from .models import Meal, Rating
from
from rest_framework import viewsets

# Create your views here.
class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
