# majors/models.py

from django.db import models
from django.urls import reverse

from courses.models import Course

class Major(models.Model):
    abbreviation = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    courses = models.ManyToManyField(Course)

    class Meta:
        ordering = ["abbreviation"]

    def __str__(self):
        return f"{self.abbreviation} - {self.name}"

    def get_absolute_url(self):
        return reverse("major_detail", args=[str(self.slug)])
