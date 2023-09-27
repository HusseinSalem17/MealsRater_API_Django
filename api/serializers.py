from rest_framework import serializers
from .models import Meal, Rating
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password")
        # to make password write only not readable or back to frontend in json
        extra_kwargs = {"password": {"write_only": True, "required": True}}

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ("id", "title", "description", "no_of_ratings", "avg_rating")


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ("id", "stars", "user", "meal")
