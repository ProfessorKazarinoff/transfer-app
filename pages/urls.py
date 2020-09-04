# pages/urls.py

from django.urls import path
from .views import HomePageListView, AboutPageView

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageListView.as_view(), name="home"),
]
