# courses/views.py

from django.views.generic import ListView, DetailView

from .models import Course
from colleges.models import College
from majors.models import Major


class CourseDetailView(DetailView):
    model = Course
    template_name = "course_detail.html"


class CourseListView(ListView):
    model = Course
    template_name = "course_list.html"

class CollegeDetailView(DetailView):
    model = College
    template_name = "college_detail.html"


class CollegeListView(ListView):
    model = College
    template_name = "college_list.html"
