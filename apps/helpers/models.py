from django.db import models
from apps.bands.models import Band
from apps.users.models import User

class User_Band(models.Model):
	band = models.ForeignKey(Band)
	user = models.ForeignKey(User)
	user_level = models.ForeignKey('User_level')

	class Meta:
		db_table = "users_has_bands"


class User_level(models.Model):
	name = models.CharField(max_length=100)

	class Meta:
		db_table = "user_levels"


class Rule(models.Model):
	# put some rules in here
	# Right now this table's just floating around
	class Meta:
		db_table = "rules"