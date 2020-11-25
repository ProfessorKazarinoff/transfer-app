# colleges/models.py

from django.db import models
from django.urls import reverse
from majors.models import Major


class College(models.Model):
    abbreviation = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=200, null=True, blank=True)
    slug = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    majors = models.ManyToManyField(Major)
    is_2year = models.BooleanField(null=True, blank=True)
    is_4year = models.BooleanField(null=True, blank=True)

    class Meta:
        ordering = ["abbreviation"]

    def __str__(self):
        return f"{self.abbreviation} - {self.name}"

    def get_absolute_url(self):
        return reverse("college_detail", args=[str(self.slug)])
