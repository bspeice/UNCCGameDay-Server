from models import ParkingLot, ParkingRating
from serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
	"""

	def post(self, request):
		rating = ParkingRatingSerializer(data=request.DATA)
		if rating.is_valid():
			rating.save()
			return Response(rating.data)
		return Response(rating.errors, status=status.HTTP_400_BAD_REQUEST)