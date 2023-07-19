from django.conf.urls import include
from django.contrib import admin
from products import views
from django.urls import path

urlpatterns = [
    path(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),
]