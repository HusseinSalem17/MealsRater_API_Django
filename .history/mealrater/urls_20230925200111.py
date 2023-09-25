from django.contrib import admin
from django.urls import path


urlpatterns = [
    path("admin/", admin.site.urls),
    
    # api url
    path("api/", include("api.urls")),  
]

