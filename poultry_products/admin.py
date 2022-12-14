from django.contrib import admin
from poultry_products.models import Governorate, ProductName, Product, ProductCate



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = [field.name for field in Product._meta.get_fields()]

    search_fields = list_display

    list_filter = list_display
    list_per_page = 300  # No of records per page



@admin.register(Governorate)
class GovernorateAdmin(admin.ModelAdmin):

    list_display = ["name",]

    search_fields = list_display

    list_filter = list_display
    list_per_page = 300  # No of records per page


@admin.register(ProductName)
class ProductNameAdmin(admin.ModelAdmin):

    list_display = ["name",]

    search_fields = list_display

    list_filter = list_display
    list_per_page = 300  # No of records per page

@admin.register(ProductCate)
class ProductCateAdmin(admin.ModelAdmin):

    list_display = ["name",]

    search_fields = list_display

    list_filter = list_display
    list_per_page = 300  # No of records per page
