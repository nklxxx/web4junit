from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^(?P<path>[a-zA-Z0-9.]+)$', views.page),
    url(r'^(?P<path>[a-zA-Z0-9.]+)/(?P<name>.*)$', views.table),
)
