from django.contrib import admin
from .models import Project, Release

admin.site.register(Project)
admin.site.register(Release)