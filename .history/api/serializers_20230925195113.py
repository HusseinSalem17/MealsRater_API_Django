from rest_framework import serializers
from .models import Meal, Rating

class MealSerializer(serializers.Serializer):
    