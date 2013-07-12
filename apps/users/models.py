from django.db import models

class User(models.Model):
	name = models.CharField(max_length=100)
	phone_number = models.IntegerField()
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField()

	class Meta:
		db_table = "users"

	def __unicode__(self):
		return self.name