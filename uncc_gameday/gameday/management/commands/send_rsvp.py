from datetime import datetime, timedelta

from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from gameday.models import RegisteredUser

class Command(BaseCommand):

	def handle(self, *args, **kwargs):
		subject = 'Students who RSVP\'ed to the game on %s:' %\
			datetime.today().date()
		from_ = 'rsvp@uncc-gameday.no-ip.org'
		recipient_list = ['bspeice.nc@gmail.com']

		message = 'The following people have registered as attending the game:\n\n'
		
		for user in RegisteredUser.objects.filter(date_registered__gt=
				(datetime.today() - timedelta(7))):
			message += user.first_name + ' ' + user.last_name + '\n'

		send_mail(subject, message, from_,recipient_list)
