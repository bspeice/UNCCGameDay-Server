from models import ParkingLot
from serializers import ParkingLotSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

class ParkingLotList(APIView):
	"""
	List all parking lots
	"""

	def get(self, request):
		parking_lots = ParkingLot.objects.all()
		serializer = ParkingLotSerializer(parking_lots, many=True)
		return Response(serializer.data)