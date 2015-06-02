from django.conf.urls import patterns, include, url
from django.contrib import admin
from app import urls as app_urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    url(r'^app/', include(app_urls)),

    # url(r'^admin/', include(admin.site.urls)),
)