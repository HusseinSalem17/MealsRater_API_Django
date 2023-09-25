from django.contrib import admin


# Register your models here.
class RatingAdmin(admin.ModelAdmin):
    list_display = ("id", "meal", "user", "stars")
    list_filter = ("meal", "user")
    
class MealAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")
    list_filter = ("title",'description')
    list_filter
