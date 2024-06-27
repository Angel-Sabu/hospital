# Generated by Django 4.2.7 on 2023-12-08 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalBackend', '0010_delete_labdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaborataryDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Testname', models.CharField(blank=True, max_length=100, null=True)),
                ('Description', models.CharField(blank=True, max_length=100, null=True)),
                ('Testimages', models.ImageField(blank=True, null=True, upload_to='Testimages')),
            ],
        ),
    ]
