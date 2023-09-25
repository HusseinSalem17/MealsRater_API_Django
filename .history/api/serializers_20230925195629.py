from rest_framework import serializers
from .models import Meal, Rating

from rest_framework.authtoken.views import obtain_auth_token

class MealSerializer(serializers.Serializer):
    class Meta:
        model = Meal
        fields = ("id", "title", "description")


class RatingSerializer(serializers.Serializer):
    class Meta:
        model = Rating
        fields = ("id", "stars", "user", "meal")
