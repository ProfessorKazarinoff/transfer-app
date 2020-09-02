# courses/views.py
from django.views.generic import ListView
from .models import Course


class MeCourseView(ListView):
    model = Course
    template_name = "me.html"
