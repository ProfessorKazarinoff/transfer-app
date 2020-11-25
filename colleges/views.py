# colleges/views.py

from django.views.generic import ListView, DetailView

from .models import College


class CollegeDetailView(DetailView):
    model = College
    template_name = "college_detail.html"


class CollegeListView(ListView):
    model = College
    template_name = "college_list.html"
