"""chicken_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("profile/", include("user_profile.urls")),
    path("api-auth/", include("rest_framework.urls")),
    
    path("equipment/", include("equipment.urls")),
    path("feed/", include("feed.urls")),
    path("poultry_products/", include("poultry_products.urls")),
    path("stations_and_ward_rent/", include("stations_and_ward_rent.urls")),
    path("veterinary_medicine/", include("veterinary_medicine.urls")),



]

admin.site.site_header = "Chicken Backend"  # default: "Django Administration"
admin.site.index_title = "Chicken Backend"  # default: "Site administration"
admin.site.site_title = "Chicken Backend"  # default: "Django site admin"
