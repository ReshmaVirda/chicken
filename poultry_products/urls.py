from django.urls import include, path
from poultry_products.views import UpdateView, DeleteView, ListView

urlpatterns = [
    path(
        "list/",
        ListView.as_view(),
    ),
    path(
        "update/<int:id>/",
        UpdateView.as_view(),
    ),
    path(
        "delete/<int:id>/",
        DeleteView.as_view(),
    ),
]
