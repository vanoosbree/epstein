from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import validate_email

class registration_form(UserCreationForm):
	first_name = forms.CharField( max_length=200, label='First Name' )
	last_name  = forms.CharField( max_length=200, label='Last Name' )
	email = forms.CharField( max_length=250, label='Email', validators=[validate_email] )

	def save(self, *args, **kwargs):
		user = super( registration_form, self ).save()
		user.email = self.cleaned_data["email"]
		user.first_name = self.cleaned_data["first_name"]
		user.last_name = self.cleaned_data["last_name"]
		user.save()