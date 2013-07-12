from django.db import models
from apps.users.models import User

class Venue(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=100)
	address = models.TextField()	
	zip_code = models.IntegerField()
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField()

	class Meta:
		db_table = "venues"

	# def __unicode__(self):
	# 	return self.name