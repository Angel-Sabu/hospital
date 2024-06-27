# Generated by Django 3.2.10 on 2023-11-29 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalFrontend', '0005_remove_contactdb_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoinmentdb',
            name='patientnumber',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contactdb',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contactdb',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
