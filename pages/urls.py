# pages/urls.py

from django.urls import path
from .views import HomePageView, MajorsPageView, HomePageListView

urlpatterns = [
    path("major_list/", MajorsPageView.as_view(), name="major_list"),
    path("", HomePageListView.as_view(), name="home"),
]
