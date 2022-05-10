from django.contrib import admin

from .models import Profile

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = [field.name for field in Profile._meta.get_fields()]
    search_fields = list_display

    list_filter = list_display
    list_per_page = 300  # No of records per page
