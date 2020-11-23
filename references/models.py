# references/models.py

from django.db import models
from django.urls import reverse


class Reference(models.Model):
    url = models.URLField(max_length=200)
    description = models.CharField(max_length=80, null=True, blank=True)
    slug = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        ordering = ["description"]

    def __str__(self):
        return f"{self.description} - {str(self.url)}"

    def get_absolute_url(self):
        return reverse("reference_link_detail", args=[str(self.slug)])
