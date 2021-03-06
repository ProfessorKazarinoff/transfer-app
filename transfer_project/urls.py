# transfer_project/urls.py

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", include("pages.urls")),
    path("courses/", include("courses.urls")),
    path("majors/", include("majors.urls")),
    path("colleges/", include("colleges.urls")),
    path("admin/", admin.site.urls),
]
