# pages/urls.py

from django.urls import path
from .views import HomePageView, MePageView, CivePageView, EePageView

urlpatterns = [
    path("me/", MePageView.as_view(), name="me"),
    path("cive/", CivePageView.as_view(), name="cive"),
    path("ee/", EePageView.as_view(), name="ee"),
    path("", HomePageView.as_view(), name="home"),
]
