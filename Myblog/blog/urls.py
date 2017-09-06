from django.conf.urls import url
from django.contrib import admin
from blog import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$/', views.index),
    url(r'^archive/$', views.archive),
    url(r'^article/$', views.article),
    url(r'^comment/post/$', views.comment_post),
    url(r'^logout/$', views.do_logout),
    url(r'^login', views.do_login),
    url(r'^reg', views.do_reg),
    url(r'^category/$', views.category),
]