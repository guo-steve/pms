from django.contrib import admin

from .models import MeterialsDescription, VisualFormFactor, BusinessCategory, ModuleCode

admin.site.register(MeterialsDescription)
admin.site.register(VisualFormFactor)
admin.site.register(BusinessCategory)
admin.site.register(ModuleCode)
