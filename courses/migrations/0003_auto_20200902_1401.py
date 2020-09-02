# Generated by Django 3.1.1 on 2020-09-02 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20200826_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='in_bioe',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='in_cheme',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='in_cive',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='in_ee',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='in_enviro',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='in_me',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='in_mse',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
