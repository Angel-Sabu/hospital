from django.db import models


# Create your models here.

class signupDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Username = models.CharField(max_length=100, null=True, blank=True)
    RegPassword = models.CharField(max_length=100, null=True, blank=True)


class appoinmentDB(models.Model):
    patientname = models.CharField(max_length=100, null=True, blank=True)
    patientdob = models.DateField(max_length=100, null=True, blank=True)
    AppoinmentDate = models.DateField(max_length=100, null=True, blank=True)
    patienttime = models.TimeField(max_length=100, null=True, blank=True)
    patientnumber = models.CharField(max_length=10, null=True, blank=True)
    patientdes = models.CharField(max_length=100, null=True, blank=True)
    UserName = models.CharField(max_length=100, null=True, blank=True)
    Departmentname = models.CharField(max_length=100, null=True, blank=True)
    doc_name = models.CharField(max_length=100, null=True, blank=True)
    Status = models.CharField(max_length=100, null=True, blank=True)


class contactDB(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    message = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)


class feedbackDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Feedback = models.CharField(max_length=100, null=True, blank=True)


class LabappoDB(models.Model):
    patientsname = models.CharField(max_length=100, null=True, blank=True)
    patientsdob = models.DateField(max_length=100, null=True, blank=True)
    patientstime = models.TimeField(max_length=100, null=True, blank=True)
    patientsnumber = models.CharField(max_length=10, null=True, blank=True)
    patientsdes = models.CharField(max_length=100, null=True, blank=True)
    UserName = models.CharField(max_length=100, null=True, blank=True)
    Testname = models.CharField(max_length=100, null=True, blank=True)
    Status = models.CharField(max_length=100, null=True, blank=True)
