from django.db import models

from datetime import datetime

# Create your models here.
class RegisteredUser(models.Model):

	date_registered = models.DateTimeField(default=datetime.now)
	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)
	section = models.CharField(max_length=8, null=True, blank=True)
	row = models.IntegerField(null=True, blank=True)

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

	LOT_ENTRANCES = {
		# Put the parking lot entrances here. Something like:
		# PARKING_LOT: (<latitude>, <longitude>, <label>),
		LOT_GOLD: (35.31255, -80.74297, 'Gold Entrance'), # Lower Tryon
		LOT_GREEN: (35.31255, -80.74297, 'Green Entrance'), # Lower Tryon
		LOT_BLACK: (35.31698, -80.72668, 'Black Entrance'), # Mallard Creek
		LOT_RED: (35.30185, -80.74655, 'Red Entrance'), # Toby Creek / Harris
		LOT_BLUE: (35.29884, -80.73715, 'Blue Entrance'), # Cameron Blvd.
		LOT_SILVER: (35.31698, -80.72668, 'Silver Entrance'), # Mallard Creek
		LOT_ORANGE: (35.31255, -80.74297, 'Orange Entrance'), # Lower Tryon
		LOT_YELLOW: (35.31698, -80.72668, 'Yellow Entrance'), # Mallard Creek
		LOT_PURPLE: (35.30185, -80.74655, 'Purple Entrance'), # Toby Creek / Harris
		LOT_PINK: (35.30147, -80.73140, 'Pink Entrance'), # Campus Main Entrance
		LOT_WHITE: (35.30725, -80.72470, 'White Entrance'), # John Kirk
	}

	# Only one ParkingLot per location
	location = models.CharField(choices=LOT_CHOICES, unique=True,
								primary_key=True, max_length=8)
	# parkingrating_set
	
	@property
	def current_ratings(self):
		# Return a QuerySet containing only valid ParkingRatings
		# (those ratings that aren't from a previous gameday)
		return self.parkingrating_set.all()
	
	def get_rating(self):
		# Get the current rating of this parking lot
		NUM_LOTS = 10
		if self.current_ratings.count() < NUM_LOTS:
			return None
		else:
			total = sum([ ParkingRating.RATING_WEIGHTS[r.rating]
				for r in self.parkingrating_set.all().order_by('-created')[0:10] ])
			return total / NUM_LOTS

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
	RATING_WEIGHTS = {
		RATING_EMPTY: 0,
		RATING_SCATTERED: 33,
		RATING_BUSY: 66,
		RATING_FULL: 100,
	}

	rating = models.CharField(max_length=3, choices=RATING_CHOICES)
	created = models.DateTimeField(default=datetime.now)
	parking_lot = models.ForeignKey(ParkingLot)
