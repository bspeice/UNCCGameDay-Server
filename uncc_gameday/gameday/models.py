from django.db import models

from datetime import datetime

# Create your models here.
class RegisteredUser(models.Model):

	date_registered = models.DateTimeField()
	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)
	section = models.CharField(max_length=8)
	row = models.IntegerField()

class ParkingLot(models.Model):

	LOT_GOLD = 'GOLD'
	LOT_GREEN = 'GREEN'
	LOT_BLACK = 'BLACK'
	LOT_RED = 'RED'
	LOT_BLUE = 'BLUE'
	LOT_SILVER = 'SILVER'
	LOT_ORANGE = 'ORANGE'
	LOT_YELLOW = 'YELLOW'
	LOT_PURPLE = 'PURPLE'
	LOT_PINK = 'PINK'
	LOT_WHITE = 'WHITE'
	LOT_CHOICES = (
		(LOT_GREEN, 'Green'),
		(LOT_BLACK, 'Black'),
		(LOT_RED, 'Red'),
		(LOT_BLUE, 'Blue'),
		(LOT_SILVER, 'Silver'),
		(LOT_ORANGE, 'Orange'),
		(LOT_YELLOW, 'Yellow'),
		(LOT_PURPLE, 'Purple'),
		(LOT_PINK, 'Pink'),
		(LOT_WHITE, 'White'),
		(LOT_GOLD, 'Gold'),
	)

	LOT_LOCATIONS = (
		# Put the parking lot locations here. Something like:
		# (LOT_GREEN, '(11.23.43, 11.83.12)'),
		(None, None),
	)

	# Only one ParkingLot per location
	location = models.CharField(choices=LOT_CHOICES, unique=True,
								primary_key=True)
	# parkingrating_set

class ParkingRating(models.Model):

	RATING_EMPTY = 'EMP'
	RATING_SCATTERED = 'SCT'
	RATING_BUSY = 'BSY'
	RATING_FULL = 'FLL'
	RATING_CHOICES = (
		(RATING_EMPTY, 'Empty'),
		(RATING_SCATTERED, 'Scattered'),
		(RATING_BUSY, 'Busy'),
		(RATING_FULL, 'Full'),
	)

	rating = models.CharField(max_length=10, choices=RATING_CHOICES)
	created = models.DateTimeField(default=datetime.datetime.now)
	parking_lot = models.ForeignKey(ParkingLot)