# pages/views.py

from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class MajorsPageView(TemplateView):
    template_name = "majors_list.html"
