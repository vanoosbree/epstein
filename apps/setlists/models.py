from django.db import models
from apps.events.models import Event
from datetime import datetime 

class Setlist(models.Model):
	event = models.ForeignKey(Event)
	songs = models.CharField(max_length=255)
	created_at = models.DateTimeField( default=datetime.now, blank=True )
	updated_at = models.DateTimeField( default=datetime.now, blank=True )

	class Meta:
		db_table = "setlist"

	# def __unicode__(self):
	# 	return self.title