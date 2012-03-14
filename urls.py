from django.conf.urls.defaults import patterns, include, url
from myproject.council_pay import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
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
)
