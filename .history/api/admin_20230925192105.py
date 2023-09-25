from django.contrib import admin

# Register your models here.
class RatingAdmin(admin.ModelAdmin):
    list_display = ("meal", "user", "stars")
    search_fields = ("meal", "user", "stars")