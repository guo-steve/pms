from django.conf.urls import url
import views

urlpatterns = [
    url(r'^hello$', views.hello),
    url(r'^ajax$', views.ajax),
    url(r'^$', views.index),
]