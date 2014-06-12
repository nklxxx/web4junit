from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'web4junit.views.home', name='home'),
    url(r'^testdata/', include('testdata.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
