from django.urls
from rest_framework import routers
from django.conf.urls import include
from .views import MealViewSet, RatingViewSet

router=routers.DefaultRouter()
router.register('meals', MealViewSet)