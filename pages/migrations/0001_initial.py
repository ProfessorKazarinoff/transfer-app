# Generated by Django 3.1.1 on 2020-11-23 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ReferenceLink",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.URLField()),
                ("description", models.CharField(blank=True, max_length=80, null=True)),
                ("slug", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "college",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="courses.college",
                    ),
                ),
            ],
            options={"ordering": ["college"],},
        ),
    ]
