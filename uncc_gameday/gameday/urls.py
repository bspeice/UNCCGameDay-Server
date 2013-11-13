from django.conf.urls import url, patterns
import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('gameday.views',
	url('^$', 'api_root'),
	url('^lots/$', views.ParkingLotList.as_view(), name='parking-lots'),
	url('^lots/rate/$', views.RateLot.as_view(), name='parking-rating'),
	url('^lots/location/(?P<lot>\w+)/$', views.ParkingLotEntrance.as_view(), name='get-location'),
	url('^lots/(?P<lot>\w+)/$', views.SingleParkingLotList.as_view(), name='parking-lot'),
	url('^register/(?P<id>\d+)/$', views.ListRegisteredUsers.as_view(), name='get-registered-user'),
	url('^register/(?P<fname>\w+)/(?P<lname>\w+)/$', views.ListRegisteredUserByName.as_view(),
		name='get-registered-user-by-name'),
	url('^register/$', views.RegisterUser.as_view(), name='register-user'),
)
