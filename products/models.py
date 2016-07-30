from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from common.models import BusinessCategory

def get_file_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/products/<code><ext>
    return os.path.join('products', instance.code + os.path.splitext(filename)[1])

class ProductType(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20)
    description = models.TextField()
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT)
    business_category = models.ForeignKey(BusinessCategory, on_delete=models.PROTECT)
    instruction_file = models.FileField(upload_to=get_file_path)
    active = models.BooleanField(default=True)
    creation_date = models.DateTimeField(default=timezone.now, editable=False)
    def __str__(self):
        return self.name
