from django.contrib import admin
from stations_and_ward_rent.models import StationAndWard

@admin.register(StationAndWard)
class StationAndWardAdmin(admin.ModelAdmin):

    list_display = ["product_name",]

    search_fields = list_display

    list_filter = list_display
    list_per_page = 300  # No of records per page
