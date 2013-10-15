# Any code below will be run exactly once on import.
# Basically, we run whenever the root URLconf is loaded.

from gameday.models import ParkingLot
if ParkingLot.objects.all().count() == 0:
	for location in ParkingLot.LOT_CHOICES:
		ParkingLot.objects.create(location=location)