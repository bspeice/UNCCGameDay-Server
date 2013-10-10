from django.db import models

# Create your models here.
class RegisteredUser(models.Model):

	date_registered = models.DateTimeField()
	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)
	section = models.CharField(max_length=8)
	row = models.IntegerField()