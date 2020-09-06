from django.contrib import admin

from .models import Course, Major, College

admin.site.register(Course)
admin.site.register(Major)
admin.site.register(College)
