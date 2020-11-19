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
    slug = models.CharField(max_length=10, null=True, blank=True)
    course_name = models.CharField(max_length=50)
    credits = models.FloatField()
    course_type = models.CharField(
        max_length=5, choices=COURSE_TYPE_CHOICES, default=ENGR
    )
    osu_equivalent = models.CharField(max_length=50)
    psu_equivalent = models.CharField(max_length=50)
    oit_equivalent = models.CharField(max_length=50)
    up_equivalent = models.CharField(max_length=50, null=True, blank=True)
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

    description = models.TextField(max_length=1000, null=True, blank=True)

    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["course_number"]

    def __str__(self):
        return f"{self.course_number} - {self.course_name}"

    def get_absolute_url(self):
        return reverse("course_detail", args=[str(self.slug)])


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


class College(models.Model):
    abbreviation = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    is_2year = models.BooleanField(null=True, blank=True)
    is_4year = models.BooleanField(null=True, blank=True)
    majors = models.ManyToManyField(Major)

    class Meta:
        ordering = ["abbreviation"]

    def __str__(self):
        return f"{self.abbreviation} - {self.name}"

    def get_absolute_url(self):
        return reverse("college_detail", args=[str(self.slug)])
