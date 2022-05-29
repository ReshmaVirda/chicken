from django.contrib import admin

# Register your models here.
from django.contrib import admin
from veterinary_medicine.models import   VeterinaryMadicine



@admin.register(VeterinaryMadicine)
class VeterinaryMadicineAdmin(admin.ModelAdmin):

    list_display = ["product_name",]

    search_fields = list_display

    list_filter = list_display
    list_per_page = 300  # No of records per page
