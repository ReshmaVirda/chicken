from django.contrib import admin
from equipment.models import  ProductEquipment

# Register your models here.


@admin.register(ProductEquipment)
class ProductFeedAdmin(admin.ModelAdmin):

    list_display = [field.name for field in ProductEquipment._meta.get_fields()]

    search_fields = list_display

    list_filter = list_display
    list_per_page = 300  # No of records per page
