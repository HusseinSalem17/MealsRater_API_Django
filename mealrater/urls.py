from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("admin/", admin.site.urls),
    # api url
    path("api/", include("api.urls")),
    path("tokerequest/", obtain_auth_token),
]
