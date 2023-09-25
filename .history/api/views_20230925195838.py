from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    
