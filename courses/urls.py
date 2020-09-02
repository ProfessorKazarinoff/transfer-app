# courses/urls.py

from django.urls import path
from .views import MeCourseListView, CiveCourseListView, EeCourseListView

urlpatterns = [
    path("me/", MeCourseListView.as_view(), name="me_course_list"),
    path("cive/", CiveCourseListView.as_view(), name="cive_course_list"),
    path("ee/", EeCourseListView.as_view(), name="ee_course_list"),
]
