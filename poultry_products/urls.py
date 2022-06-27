from django.urls import include, path
from poultry_products.views import (
    UpdateView,
    DeleteView,
    ListView,
    DetailView,
    CreateView,
    ProductNameListView,
    ProductCateListView,
    GoverListView
)

urlpatterns = [
    path(
        "list/",
        ListView.as_view(),
    ),
    
    path(
        "product-cate/",
        ProductCateListView.as_view(),
    ),
    path(
        "product-names/",
        ProductNameListView.as_view(),
    ),
    path(
        "governorate/",
        GoverListView.as_view(),
    ),
    
    path(
        "update/<int:id>/",
        UpdateView.as_view(),
    ),
    path(
        "create/",
        CreateView.as_view(),
    ),
    path(
        "detail/<int:id>/",
        DetailView.as_view(),
    ),
    path(
        "delete/<int:id>/",
        DeleteView.as_view(),
    ),
]
