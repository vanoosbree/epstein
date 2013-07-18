from django.db import models
from apps.bands.models import Band
from apps.venues.models import Venue
from datetime import datetime 

class Event(models.Model):
	band = models.ForeignKey(Band)
	venue = models.ForeignKey(Venue)
	type = models.CharField(max_length=100)
	date = models.DateTimeField()
	time = models.TimeField()
	description = models.TextField()
	address = models.TextField()	
	created_at = models.DateTimeField( default=datetime.now, blank=True )
	updated_at = models.DateTimeField( default=datetime.now, blank=True )

	class Meta:
		db_table = "events"
       
	# def __unicode__(self):
	# 	return self.name