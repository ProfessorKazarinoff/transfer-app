# pages/views.py

from django.views.generic import TemplateView, ListView
from courses.models import Major

class HomePageView(TemplateView):
    template_name = "home.html"

class HomePageListView(ListView):
    template_name = "home.html"
    model = Major

class MajorsPageView(TemplateView):
    template_name = "majors_list.html"
