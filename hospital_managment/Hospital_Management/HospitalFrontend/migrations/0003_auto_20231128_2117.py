# Generated by Django 3.2.10 on 2023-11-28 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalFrontend', '0002_appoinmentdb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appoinmentdb',
            old_name='Departmentname',
            new_name='UserName',
        ),
        migrations.RemoveField(
            model_name='appoinmentdb',
            name='doc_name',
        ),
    ]
