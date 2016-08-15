from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from common.models import MeterialsDescription, VisualFormFactor, BusinessCategory
from documents.models import Document
from products.models import ProductType, Product
from orders.models import DataBatch
from customers.models import Operator

class Project(models.Model):
    code = models.CharField(max_length=15)
    name = models.CharField(max_length=255)
    description = models.TextField()
    customer = models.ForeignKey(Operator, on_delete=models.PROTECT)
    materials_description = models.ForeignKey(MeterialsDescription, on_delete=models.PROTECT)
    visual_form_factor = models.ForeignKey(VisualFormFactor, on_delete=models.PROTECT)
    business_category = models.ForeignKey(BusinessCategory, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    documents = models.ManyToManyField(Document)
    update_date = models.DateTimeField(auto_now=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.code + self.name

class Release(models.Model):
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    data_batch = models.ForeignKey(DataBatch, on_delete=models.PROTECT)
    def __str__(self):
        return self.project.code + "_" + self.data_batch.batch_number

#class CRS(models.Model):
    # name = models.CharField(max_length=255)

    # artwork_code =
    # module_code =
    # delivery_packing
    # packaging_material
    # labelling_data
    # packing_list
    # scratch_panel
    # scratch_panel_detal
    # single_packing
    #