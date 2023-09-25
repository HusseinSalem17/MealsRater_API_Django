from .models import Meal, Rating
from .serializers import MealSerializer, RatingSerializer
from rest_framework import viewsets


# Create your views here.
# can create and delete and update 
class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
