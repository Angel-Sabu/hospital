# Generated by Django 3.2.10 on 2023-11-29 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalFrontend', '0007_contactdb_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='appoinmentdb',
            name='Departmentname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='appoinmentdb',
            name='doc_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
