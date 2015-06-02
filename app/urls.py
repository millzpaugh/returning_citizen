from django.conf.urls import patterns, include, url
from app import views as app_views
from views import index, about, resources

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    url(r'^index/', index, name='index'),
    url(r'^about/', about, name='about'),
    url(r'^resources/', resources, name='resources')
    # url(r'^admin/', include(admin.site.urls)),
)