from django.db import models


# Create your models here.
class DepDB(models.Model):
    Departmentname = models.CharField(max_length=100, null=True, blank=True)
    Description = models.TextField(max_length=300, null=True, blank=True)
    Services = models.TextField(max_length=300, null=True, blank=True)
    DepartmentImages = models.ImageField(upload_to="CategoryImage", null=True, blank=True)


class DoctorDB(models.Model):
    doc_name = models.CharField(max_length=100, null=True, blank=True)
    doc_spec = models.CharField(max_length=100, null=True, blank=True)
    doc_desc = models.CharField(max_length=100, null=True, blank=True)
    Departmentname = models.CharField(max_length=100, null=True, blank=True)
    doc_image = models.ImageField(upload_to="CategoryImage", null=True, blank=True)


class LaborataryDB(models.Model):
    Testname = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Testimages = models.ImageField(upload_to="Testimages", null=True, blank=True)
