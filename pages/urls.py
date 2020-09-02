# pages/urls.py

from django.urls import path
from .views import HomePageView, MajorsPageView

urlpatterns = [
    path("major_list/", MajorsPageView.as_view(), name="major_list"),
    path("", HomePageView.as_view(), name="home"),
]
