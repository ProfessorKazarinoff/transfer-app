# pages/urls.py

from django.urls import path
from .views import HomePageView, MePageView

urlpatterns = [
    path("me/", MePageView.as_view(), name="me"),
    path("", HomePageView.as_view(), name="home"),
]
