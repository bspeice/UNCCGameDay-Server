from django.conf.urls import url, patterns
import views

urlpatterns = patterns('gameday.views',
	url('^$', 'api_root'),
	url('^lots/$', views.ParkingLotList.as_view(), name='parking-lots'),
	url('^rate/$', views.RateLot.as_view(), name='parking-rating'),
)