from django.db import models
from apps.bands.models import Band
from apps.venues.models import Venue

class Event(models.Model):
	band = models.ForeignKey(Band)
	venue = models.ForeignKey(Venue)
	type = models.CharField(max_length=100)
	date = models.DateTimeField()
	time = models.TimeField()
	description = models.TextField()
	address = models.TextField()	
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField()

	class Meta:
		db_table = "events"

	# def __unicode__(self):
	# 	return self.name