# pages/views.py

from django.views.generic import TemplateView, ListView

from majors.models import Major


class HomePageListView(ListView):
    template_name = "home.html"
    model = Major


class AboutPageView(TemplateView):
    template_name = "about.html"
