# pages/views.py

from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"

class MePageView(TemplateView):
    template_name = "me.html"

class CivePageView(TemplateView):
    template_name = "cive.html"

class EePageView(TemplateView):
    template_name = "ee.html"
