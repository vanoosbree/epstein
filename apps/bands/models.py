from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User

class Band(models.Model):
	name 		= models.CharField(max_length=100)
	members 	= models.ManyToManyField( User, through='UserHasBand')
	created_at 	= models.DateTimeField( default=datetime.now, blank=True )
	updated_at 	= models.DateTimeField( default=datetime.now, blank=True)
	
	class Meta:
		db_table = "bands"

	def __unicode__(self):
		return self.name

class UserHasBand(models.Model):
	user = models.ForeignKey(User)
	band = models.ForeignKey(Band)
	user_level_id = models.IntegerField(default=0)

	class Meta:
		db_table = "users_has_bands"