from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import MealViewSet, RatingViewSet, UserViewSet

router = routers.DefaultRouter()
router.register("meals", MealViewSet)
router.register("ratings", RatingViewSet)
router.register("users", UserViewSet, basename="users")
urlpatterns = [
    path("", include(router.urls)),
]
