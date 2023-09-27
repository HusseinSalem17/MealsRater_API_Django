from .models import Meal, Rating
from .serializers import MealSerializer, RatingSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.authtoken.models import Token


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def create(self, request,*args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        response = {
            "Token": f"Token {token.key}",
        }
        return Response(response, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        response = {
            "message": "you can't list users like that",
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
# can create and delete and update and read using ModelViewSet
class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # to make business logic not in the model like update or create or destroy or list or retrieve nedd to use (@action) decorator (to modify the class viewSets)
    # detail = True to be able to change the value of this function
    @action(detail=True, methods=["POST"])
    def rate_meal(self, request, pk=None):
        if "stars" in request.data:
            """
            create or update
            """
            # get the pk from the url
            meal = Meal.objects.get(id=pk)
            # get the user from the token
            user = request.user
            print(user)
            # request means from body (postman)
            # username = request.data["username"]
            # user = User.objects.get(username=username)
            stars = request.data["stars"]
            try:
                # update
                rate = Rating.objects.get(meal=meal.id, user=user.id)
                rate.stars = stars
                rate.save()
                serializer = RatingSerializer(rate, many=False)
                json = {
                    "message": "rating updated",
                    "result": serializer.data,
                }
                return Response(json, status=status.HTTP_200_OK)
            except Exception:
                # create (if the rate not exist)
                rate = Rating.objects.create(meal=meal, user=user, stars=stars)
                serializer = RatingSerializer(rate, many=False)
                json = {
                    "message": "rating created",
                    "result": serializer.data,
                }
                return Response(json, status=status.HTTP_200_OK)
        else:
            json = {
                "message": "you need to provide stars",
            }
            return Response(json, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # disable create and update and delete (override on update and create methods)
    def update(self, request, *args, **kwargs):
        response = {
            "message": "you can't update rating like that",
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {
            "message": "you can't update rating like that",
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
