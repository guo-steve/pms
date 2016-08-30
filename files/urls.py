from django.conf.urls import url
from . import views

app_name = 'files'

urlpatterns = [
    url(r'^(?P<file_name>.+)$', views.download, name='download'),
]
