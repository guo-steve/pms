from django.conf.urls import url
from . import views

app_name = 'orders'
urlpatterns = [
    url(r'^hello$', views.hello),
    url(r'^$', views.orders, name='index'),
    url(r'^ajax$', views.orders_ajax, name='ajax'),
    url(r'^(?P<order_id>\d+)/$', views.orders_detail, name='detail'),
    url(r'^(?P<order_id>\d+)/data_batches/$', views.data_batches, name='data_batches'),
    url(r'^(?P<file_name>.+)$', views.order_original_file, name='original_file'),
]
