from django.conf.urls import url, patterns
import views

urlpatterns = patterns('',
	url('^lots/$', views.ParkingLotList.as_view())
)