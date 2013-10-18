from django.conf.urls import url, patterns
import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('gameday.views',
	url('^$', 'api_root'),
	url('^lots/$', views.ParkingLotList.as_view(), name='parking-lots'),
	url('^lots/(?P<lot>\w+)/$', views.SingleParkingLotList.as_view(), name='parking-lot'),
	url('^rate/$', views.RateLot.as_view(), name='parking-rating'),
)
