from django.db import models
from apps.events.models import Event

class Setlist(models.Model):
	event = models.ForeignKey(Event)
	songs = models.CharField(max_length=255)
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField()

	class Meta:
		db_table = "setlist"

	# def __unicode__(self):
	# 	return self.title