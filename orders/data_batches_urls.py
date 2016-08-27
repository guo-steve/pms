from django.conf.urls import url
from . import views

app_name = 'data_batches'
urlpatterns = [
    url(r'^$', views.data_batches, name='index'),
    url(r'^ajax$', views.data_batches_ajax, name='ajax'),
    url(r'^(?P<batch_id>\d+)/$', views.data_batches_detail, name='detail'),
]
