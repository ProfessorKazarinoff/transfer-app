# courses/urls.py

from django.urls import path
from .views import (
    CourseDetailView,
    CourseListView,
)

urlpatterns = [
    path("course_list/", CourseListView.as_view(), name="course_list"),
    path("course/<slug:slug>/", CourseDetailView.as_view(), name="course_detail"),
]
