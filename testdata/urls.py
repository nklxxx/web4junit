from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^(?P<path>[a-zA-Z0-9._]+)$', views.page),
    url(r'^json/save.json$', views.save),
)
