from django.urls import path
from django.urls import include, path
from image_service.views import FileUploadView
urlpatterns = [

    path(
        "create/",
        FileUploadView.as_view(),
    ),

]
