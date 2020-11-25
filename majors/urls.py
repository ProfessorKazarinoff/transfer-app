# majors/urls.py

from django.urls import path
from .views import (
    MajorDetailView,
    MajorListView,
)

urlpatterns = [
    path("major_list/", MajorListView.as_view(), name="major_list"),
    path("major/<slug:slug>/", MajorDetailView.as_view(), name="major_detail"),
]
