from django.contrib import admin


# Register your models here.
class RatingAdmin(admin.ModelAdmin):
    list_display = ("id", "meal", "user", "stars")
    list_filter = ("meal", "user")
