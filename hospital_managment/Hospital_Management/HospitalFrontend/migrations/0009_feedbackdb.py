# Generated by Django 3.2.10 on 2023-12-03 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalFrontend', '0008_auto_20231129_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedbackDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Feedback', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
