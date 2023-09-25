from rest_framework import serializers
from .models import Meal, Rating


class MealSerializer(serializers.Mode):
    class Meta:
        model = Meal
        fields = ("id", "title", "description")


class RatingSerializer(serializers.Serializer):
    class Meta:
        model = Rating
        fields = ("id", "stars", "user", "meal")
