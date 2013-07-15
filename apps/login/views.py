from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import registration_form

def register(request):
	user = success = ''
	form = registration_form(request.POST or None)

	if form.is_valid():
		form.save()
		success = True

	variable = { 'form' : form, 'success' : success }

	return render_to_response( "login/registration.html", variable, context_instance=RequestContext(request) )