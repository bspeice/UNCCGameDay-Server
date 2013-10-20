from django.forms import widgets
from rest_framework import serializers
from models import *

class ParkingLotSerializer(serializers.ModelSerializer):
	filled_pct = serializers.IntegerField(read_only=True, source='get_rating')

	class Meta:
		model = ParkingLot
		fields = ('location', 'filled_pct')

class ParkingRatingSerializer(serializers.ModelSerializer):
	class Meta:
		model = ParkingRating
		fields = ('rating', 'parking_lot',)

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = RegisteredUser
		fields = ('first_name', 'last_name', 'section', 'row')

class SingleUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = RegisteredUser
		fields = ('id', 'first_name', 'last_name')
