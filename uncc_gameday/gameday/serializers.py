from django.forms import widgets
from rest_framework import serializers
from models import *

class ParkingLotSerializer(serializers.ModelSerializer):
	filled_pct = serializers.IntegerField(read_only=True, source='get_rating')

	class Meta:
		model = ParkingLot
		fields = ('location', 'filled_pct')