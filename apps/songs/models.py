from django.db import models
from apps.bands.models import Band

class Song(models.Model):
	band = models.ForeignKey(Band)
	title = models.CharField(max_length=100)
	description = models.TextField()
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField()

	class Meta:
		db_table = "songs"

	def __unicode__(self):
		return self.title