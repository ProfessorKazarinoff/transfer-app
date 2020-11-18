# pages/models.py

from django.db import models
from django.urls import reverse

from courses.models import College

class ReferenceLink(models.Model):
    url = models.URLField(max_length=200)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    description = models.CharField(max_length=80, null=True, blank=True)
    slug = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        ordering = ["college"]

    def __str__(self):
        return f"{self.college} - {str(self.url)}"

    def get_absolute_url(self):
        return reverse("reference_link_detail", args=[str(self.slug)])
