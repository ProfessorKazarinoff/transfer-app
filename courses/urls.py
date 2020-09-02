# courses/urls.py

from django.urls import path
from .views import MeCourseView

urlpatterns = [
    path("me/", MeCourseView.as_view(), name="me_course_list"),
]
