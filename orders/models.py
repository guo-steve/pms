from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from customers.models import Operator

def get_file_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/orders/<code><ext>
    return os.path.join('products', instance.name + os.path.splitext(filename)[1])

class Order(models.Model):
    name = models.CharField(max_length=30)
    customer = models.ForeignKey(Operator, on_delete=models.PROTECT)
    order_number = models.CharField(max_length=30)
    description = models.TextField()
    quantity = models.IntegerField()
    original_file = models.FileField(upload_to=get_file_path)
    updated_date = models.DateTimeField(null=True, blank=True)
    creation_date = models.DateTimeField(default=timezone.now, editable=False)
    def __str__(self):
        return self.name

class DataBatch(models.Model):
    batch_number = models.CharField(max_length=10)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    publish_date = models.DateTimeField(default=timezone.now, editable=False)
    class Meta:
        verbose_name_plural = "data batches"
    def country(self):
        return self.order.customer.country
    def __str__(self):
        return self.country() + "_" + self.batch_number

