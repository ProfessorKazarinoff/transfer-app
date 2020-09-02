# courses/views.py

from django.views.generic import ListView
from .models import Course


class MeCourseListView(ListView):
    model = Course
    template_name = "me.html"


class CiveCourseListView(ListView):
    model = Course
    template_name = "cive.html"


class EeCourseListView(ListView):
    model = Course
    template_name = "ee.html"
