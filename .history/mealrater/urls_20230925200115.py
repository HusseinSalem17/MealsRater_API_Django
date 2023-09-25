from django.contrib import admin
from django.urls import path
from 

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # api url
    path("api/", include("api.urls")),  
]

