
from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^index/$',views.index),
    # url(r'^upload/$', views.upload),
    url(r'^upload_s/$',views.upload_save),
    url(r'^action/$',views.action),
    url(r'^report/$',views.report),
    url(r'^test/$',views.button)
]
