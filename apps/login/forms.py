from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import validate_email

class registration_form(UserCreationForm):
	first_name = forms.CharField( max_length=200, label='First Name' )
	last_name  = forms.CharField( max_length=200, label='Last Name' )
	email = forms.CharField( max_length=250, label='Email', validators=[validate_email] )

	def save(self, *args, **hwargs):
		user = super(registration_form, self).save()