# courses/views.py

from django.views.generic import ListView, DetailView
from .models import Course, Major

class CourseDetailView(DetailView):
    model = Course
    template_name = "course_detail.html"

class CourseListView(ListView):
    model = Course
    template_name = "course_list.html"


class MajorDetailView(DetailView):
    model = Major
    template_name = "major_detail.html"


class MajorListView(ListView):
    model = Major
    template_name = "major_list.html"
