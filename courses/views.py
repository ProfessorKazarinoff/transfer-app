# courses/views.py

from django.views.generic import ListView, DetailView
from .models import Course, Major


class MeCourseListView(ListView):
    model = Course
    template_name = "me.html"


class CiveCourseListView(ListView):
    model = Course
    template_name = "cive.html"


class EeCourseListView(ListView):
    model = Course
    template_name = "ee.html"


class MajorDetailView(DetailView):
    model = Major
    template_name = "major.html"


class MajorListView(ListView):
    model = Major
    template_name = "major_list.html"
