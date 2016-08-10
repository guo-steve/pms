from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

class MeterialsDescription(models.Model):
    short_name = models.CharField(max_length=50)
    long_name = models.CharField(max_length=255)
    def __str__(self):
        return self.short_name

class VisualFormFactor(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class BusinessCategory(models.Model):
    name = models.CharField(max_length=20)
    class Meta:
        verbose_name_plural = "business categories"
    def __str__(self):
        return self.name

class ModuleCode(models.Model):
    """Mask Code of the Chip"""
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    def __str__(self):
        return self.name
