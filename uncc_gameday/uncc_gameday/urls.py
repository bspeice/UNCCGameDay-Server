from django.conf.urls import patterns, include, url

# Bit of a hack, but run any one-time code
import one_shot

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uncc_gameday.views.home', name='home'),
    # url(r'^uncc_gameday/', include('uncc_gameday.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

	url(r'^gameday/', include('gameday.urls')),
	url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
)
