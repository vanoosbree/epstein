from django.db import models

class Band(models.Model):
	name = models.CharField(max_length=100)
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField()

	class Meta:
		db_table = "bands"

	def __unicode__(self):
		return self.name