from django.urls import include, path
from feed.views import (
    UpdateView,
    DeleteView,
    ListView,
    DetailView,
    CreateView,
)

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


