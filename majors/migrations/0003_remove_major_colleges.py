# Generated by Django 3.1.1 on 2020-11-25 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('majors', '0002_major_colleges'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='major',
            name='colleges',
        ),
    ]
