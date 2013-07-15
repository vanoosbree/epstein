from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import registration_form
from django.contrib.auth import logout
from django.contrib.auth import authenticate

# try to login the user
def login(request):
	email_addr = request.POST.get( 'last_name', '' )
    password = request.POST.get( 'last_name', '' )   
	user = authenticate( username=email_addr, password=password)

	if user is not None:
    	if user.is_active:
        	return render_to_response( "users/dashboard.html", variable, context_instance=RequestContext(request) )
    	else:
        	print("The password is valid, but the account has been disabled!")
	else:
    	print("The username and password were incorrect.")

# try to logout the user
def logout(request):
    logout(request)
    # Redirect to a success page.

# try to register the user
def register(request):
	user = success = ''
	form = registration_form( request.POST or None )

	if form.is_valid():
		form.save()
		success = True

	variable = { 'form' : form, 'success' : success }

	return render_to_response( "login/registration.html", variable, context_instance=RequestContext(request) )
