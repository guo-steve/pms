from django.contrib import admin
from .models import Country, Operator, Contact

admin.site.register(Country)
admin.site.register(Operator)
admin.site.register(Contact)