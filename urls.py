from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fastcon.views.home', name='home'),
    # url(r'^fastcon/', include('fastcon.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
#)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^', include('fastcon.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)