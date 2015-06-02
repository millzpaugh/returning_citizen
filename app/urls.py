from django.conf.urls import patterns, include, url
from app import views as app_views
from views import index, about, resources

urlpatterns = patterns('',
    url(r'^about/', about, name='about'),
    url(r'^resources/', resources, name='resources'),
    url(r'^', index, name='index')
    # url(r'^admin/', include(admin.site.urls)),
)