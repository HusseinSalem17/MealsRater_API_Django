from django.contrib import admin


# Register your models here.
class RatingAdmin(admin.ModelAdmin):
    list_display = ("id", "meal", "user", "stars")
    search_fields = ("meal", "user")
