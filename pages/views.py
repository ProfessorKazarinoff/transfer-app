# pages/views.py

from django.views.generic import TemplateView, ListView

from courses.models import Major
from references.models import Reference


class HomePageListView(ListView):
    template_name = "home.html"
    model = Major


class MajorsPageView(TemplateView):
    template_name = "majors_list.html"


class AboutPageView(ListView):
    template_name = "about.html"
    model = Reference
