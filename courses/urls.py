# courses/urls.py

from django.urls import path
from .views import CourseDetailView, CourseListView, MajorDetailView, MajorListView

urlpatterns = [
    path("course_list/", CourseListView.as_view(), name="course_list"),
    path("course/<slug:slug>/", CourseDetailView.as_view(), name="course_detail"),
    path("major_list/", MajorListView.as_view(), name="major_list"),
    path("major/<slug:slug>/", MajorDetailView.as_view(), name="major_detail"),
]
