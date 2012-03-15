from django.conf.urls.defaults import patterns, include, url
from myproject.council_pay import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
import os

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^myproject/', include('myproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^home/', 'myproject.council_pay.views.home'),
	 url(r'^search_form/$', 'myproject.council_pay.views.search_form'),
	 url(r'^search/$', 'myproject.council_pay.views.search'),
	 url(r'^council/?P<name>', 'myproject.council_pay.views.detail'),
	 url(r'^bonus/', 'myproject.council_pay.views.performance'),
	 url(r'^pricey/', 'myproject.council_pay.views.pricey_council'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'C:\\django_project\\myproject\\static\\'}),
    )