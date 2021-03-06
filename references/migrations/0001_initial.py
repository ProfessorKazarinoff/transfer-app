# Generated by Django 3.1.1 on 2020-11-23 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Reference",
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
            ],
            options={"ordering": ["description"],},
        ),
    ]
