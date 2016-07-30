from __future__ import unicode_literals

import os
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.contrib.auth.models import User
from customers.models import Operator

def get_doc_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<code><ext>
    return os.path.join(instance.document_type.short_name, instance.code + os.path.splitext(filename)[1])

class DocumentType(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50)
    def short_name(self):
        return self.name.lower().replace(' ', '_')
    def __str__(self):
        return self.name

class Document(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=30)
    description = models.TextField()
    document_type = models.ForeignKey(DocumentType, on_delete=models.PROTECT)
    creator = models.ForeignKey(User, on_delete=models.PROTECT)
    customer = models.ForeignKey(Operator, on_delete=models.PROTECT)
    file = models.FileField(upload_to=get_doc_path)
    active = models.BooleanField(default=True)
    update_date = models.DateTimeField(null=True, blank=True)
    creation_date = models.DateTimeField(default=timezone.now, editable=False)
    def __str__(self):
        return '{0}({1})'.format(self.name, self.code)
