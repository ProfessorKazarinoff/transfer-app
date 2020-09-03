# courses/models.py

from django.db import models
from django.urls import reverse


class Course(models.Model):
    ENGR = "ENGR"
    SCI = "SCI"
    MTH = "MTH"
    COMM = "COMM"
    GENED = "GENED"
    COURSE_TYPE_CHOICES = [
        (ENGR, "Engineering Course"),
        (SCI, "Science and Programming Course"),
        (MTH, "Mathematics Course"),
        (COMM, "Communications Course"),
        (GENED, "General Education Course"),
    ]
    course_number = models.CharField(max_length=10)
    course_name = models.CharField(max_length=50)
    credits = models.FloatField()
    course_type = models.CharField(
        max_length=5, choices=COURSE_TYPE_CHOICES, default=ENGR
    )
    osu_equivalent = models.CharField(max_length=50)
    psu_equivalent = models.CharField(max_length=50)
    oit_equivalent = models.CharField(max_length=50)
    pre_reqs = models.CharField(max_length=50)

    offered_fall = models.BooleanField(null=True, blank=True)
    offered_winter = models.BooleanField(null=True, blank=True)
    offered_spring = models.BooleanField(null=True, blank=True)
    offered_summer = models.BooleanField(null=True, blank=True)

    in_cive = models.BooleanField(null=True, blank=True, default=True)
    in_me = models.BooleanField(null=True, blank=True, default=True)
    in_ee = models.BooleanField(null=True, blank=True, default=True)
    in_cheme = models.BooleanField(null=True, blank=True, default=True)
    in_bioe = models.BooleanField(null=True, blank=True, default=True)
    in_mse = models.BooleanField(null=True, blank=True, default=True)
    in_enviroe = models.BooleanField(null=True, blank=True, default=True)

    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["course_number"]

    def __str__(self):
        return f"{self.course_number} - {self.course_name}"

    def get_absolute_url(self):
        return reverse("course_detail", args=[str(self.id)])


class Major(models.Model):
    abbreviation = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course)

    class Meta:
        ordering = ["abbreviation"]

    def __str__(self):
        return f"{self.abbreviation} - {self.name}"

    def get_absolute_url(self):
        return reverse("major_detail", args=[str(self.id)])
