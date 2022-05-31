from django.contrib import admin
from feed.models import  ProductFeed

# Register your models here.


@admin.register(ProductFeed)
class ProductFeedAdmin(admin.ModelAdmin):

    list_display = [field.name for field in ProductFeed._meta.get_fields()]

    search_fields = list_display

    list_filter = list_display
    list_per_page = 300  # No of records per page


from feed.models import ImageFile

admin.site.register(ImageFile)