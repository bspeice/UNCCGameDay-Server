from models import ParkingLot, ParkingRating
from serializers import *
from datetime import datetime, timedelta

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

@api_view(('GET',))
def api_root(request):
	'Give some information about our API'
	return Response({
		'parking_lots': request.build_absolute_uri(reverse('parking-lots')),
		#'parking_lot': request.build_absolute_uri(reverse('parking-lot')),
		'parking_rating': request.build_absolute_uri(reverse('parking-rating')),
		#'get_registered_user': request.build_absolute_uri(reverse('get-registered-user')),
		#'get_registered_user_by_name': request.build_absolute_uri(reverse('get-registered-user-by-name')),
		'register_user': request.build_absolute_uri(reverse('register-user'))
	})

class ParkingLotList(APIView):
	"""
	List all parking lots
	"""

	def get(self, request):
		parking_lots = ParkingLot.objects.all()
		serializer = ParkingLotSerializer(parking_lots, many=True)
		return Response(serializer.data)

class SingleParkingLotList(APIView):
	"""
	List a single parking lot
	"""

	def get(self, request, lot):
		parking_lot = get_object_or_404(ParkingLot, location=lot)
		return Response(ParkingLotSerializer(parking_lot).data)

class RateLot(APIView):
	"""
	Rate a parking lot  	
	**GET**: Get the rating choice options  
	**POST**: Rate a parking lot. Please POST a body similar to: {"rating": <rating\>, "parking_lot": <parking_lot\>}
	"""

	@csrf_exempt
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
		
class ParkingLotEntrance(APIView):
	"""
	Get the location of a parking lot  
	**GET**: Get the latitude, longitude, and label of a parking lot
	"""
	
	def get(self, request, lot):
		# The get_object_or_404 makes sure that it's a valid lot that will have
		# an entry in the LOT_ENTRANCES dictionary.
		parking_lot = get_object_or_404(ParkingLot, location=lot)
		lot_t = ParkingLot.LOT_ENTRANCES[lot]
		return Response({'latitude': lot_t[0], 'longitude': lot_t[1], 'label': lot_t[2]})

class RegisterUser(APIView):
	"""
	Handle Registration of users  
	**GET**: List all registered users 
	**POST**: Register a new user. Please POST the <first_name\> and <last_name\>
	"""
	def get(self, request):
		'Get the first and last names of all registered users'
		one_week = timedelta(7)
		users = RegisteredUser.objects.filter(date_registered__gt=datetime.now()-one_week)
		users_s = SingleUserSerializer(users, many=True)
		return Response(users_s.data)
	
	def post(self, request):
		'Register a new user'
		user = UserSerializer(data=request.DATA)
		if user.is_valid():
			user.save()
			return Response(user.data)
		return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

class ListRegisteredUsers(APIView):
	"""
	Get the current information of a registered user by ID
	We have a separate view set up so we can list all information about one
	user at a time (this one), and one view to get just id, first_name,
	and last_name of all users.
	"""

	def get(self, request, id):
		'Get the information for a registered user'
		user = get_object_or_404(RegisteredUser, id=id)
		return Response(UserSerializer(user).data)

class ListRegisteredUserByName(APIView):
	"""
	Get a registered user by looking up their first and last name.
	This isn't a PK lookup, so we get the one registered most recently.
	"""

	def get(self, request, fname, lname):
		'Get the information for a specified user'
		user = RegisteredUser.objects.filter(first_name=fname, last_name=lname)\
				.order_by("-id")[0]
		if user is None:
			return Response("User not found with first_name '%s' and last_name '%s'",
					status=status.HTTP_404_NOT_FOUND)
		else:
			return Response(SingleUserSerializer(user).data)
