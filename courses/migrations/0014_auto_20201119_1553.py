# Generated by Django 3.1.1 on 2020-11-19 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_auto_20200911_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='is_2year',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='college',
            name='is_4year',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
