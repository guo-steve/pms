"""pms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index),
    #url(r'^accounts/login/$', auth_views.login),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^hello/', views.hello),
    url(r'^test/', views.test),
    url(r'^orders/', include('orders.orders_urls')),
    url(r'^data_batches/', include('orders.data_batches_urls')),
    url(r'^projects/', include('projects.projects_urls')),
    url(r'^releases/', include('projects.releases_urls')),
    url(r'^documents/', include('documents.urls')),
    url(r'^products/', include('products.urls')),
    url(r'^customers/', include('customers.urls')),
    url(r'^admin/', admin.site.urls),
]
