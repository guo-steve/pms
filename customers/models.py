from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3)
    mcc = models.CharField(max_length=3)
    area_code = models.CharField(max_length=4)
    class Meta:
        verbose_name_plural = "countries"
    def __str__(self):
        return self.name

class Operator(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    code = models.CharField(max_length=5)
    def __str__(self):
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20)
    cellphone = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20, blank=True)
    work_email = models.EmailField()
    home_email = models.EmailField(blank=True)
    company = models.ForeignKey(Operator, on_delete=models.PROTECT)
    work_address = models.CharField(max_length=100)
    home_address = models.CharField(max_length=100, blank=True)
    job_title = models.CharField(max_length=20)
    birthday = models.DateField(null=True, blank=True)
    skype = models.CharField(max_length=50, blank=True)
    facebook = models.CharField(max_length=50, blank=True)
    creation_date = models.DateTimeField(default=timezone.now, editable=False)
    def __str__(self):
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name + ' / ' + self.company.name