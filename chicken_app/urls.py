from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("profile/", include("user_profile.urls")),
    path("api-auth/", include("rest_framework.urls")),
    
    path("equipment/", include("equipment.urls")),
    path("feed/", include("feed.urls")),
    path("poultry_products/", include("poultry_products.urls")),
    path("stations_and_ward_rent/", include("stations_and_ward_rent.urls")),
    path("veterinary_medicine/", include("veterinary_medicine.urls")),

    path("image_service/", include("image_service.urls")),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Chicken Backend"  # default: "Django Administration"
admin.site.index_title = "Chicken Backend"  # default: "Site administration"
admin.site.site_title = "Chicken Backend"  # default: "Django site admin"
