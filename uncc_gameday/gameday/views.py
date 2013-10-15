from models import ParkingLot, ParkingRating
from serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from django.core.urlresolvers import reverse

@api_view(('GET',))
def api_root(request):
	'Give some information about our API'
	return Response({
		'parking_lots': request.build_absolute_uri(reverse('parking-lots')),
		'parking_rating': request.build_absolute_uri(reverse('parking-rating')),
	})

class ParkingLotList(APIView):
	"""
	List all parking lots
	"""

	def get(self, request):
		parking_lots = ParkingLot.objects.all()
		serializer = ParkingLotSerializer(parking_lots, many=True)
		return Response(serializer.data)

class RateLot(APIView):
	"""
	Rate a parking lot  	
	**GET**: Get the rating choice options  
	**POST**: Rate a parking lot
	"""

	def post(self, request):
		'Rate a parking lot'
		rating = ParkingRatingSerializer(data=request.DATA)
		if rating.is_valid():
			rating.save()
			return Response(rating.data)
		return Response(rating.errors, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request):
		'Get the rating choice options'
		return Response(ParkingRating.RATING_CHOICES)