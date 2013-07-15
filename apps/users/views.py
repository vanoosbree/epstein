# Create your views here.
#from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
    my_data = {}
    return render_to_response( 'users/index.html', my_data, context_instance=RequestContext(request) )

# try to login the user
def do_login(request):
    email    = request.POST.get( 'login_email', '' )
    password = request.POST.get( 'login_password', '' )   
    user = authenticate( username=email, password=password )
  
    if user is not None:
        if user.is_active:
            login(request,user)
            return render_to_response( "users/dashboard.html", context_instance=RequestContext(request) )
        else:
            return render_to_response( "home.html", {'errors': "Account has been disabled!"}, context_instance=RequestContext(request) )
    else:
        return render_to_response( "home.html", {'errors': "Invalid email/password combo"}, context_instance=RequestContext(request) )

# try to logout the user
def do_logout(request):
    logout(request)
    return render_to_response( "home.html", context_instance=RequestContext(request) )
    
def new(request):
    my_data = {}
    return render_to_response( 'users/new.html', my_data, context_instance=RequestContext(request) )

def create(request):
    name = request.POST.get( 'name', '' )
    email = request.POST.get( 'email', '' )
    password = request.POST.get( 'password', '' )
    password_confirm = request.POST.get( 'password_confirm', '' )
    user = User.objects.create_user( email, email, password )
    user.first_name = name
    user.save()
    my_data = { "user" : user }
    return render_to_response( 'users/index.html', my_data, context_instance=RequestContext(request) )


def about(request):
    return render_to_response( 'about.html', context_instance=RequestContext(request) )

# def bands(request):
#     return render_to_response( 'bands.html', context_instance=RequestContext(request) )

def events(request):
    return render_to_response( 'events.html', context_instance=RequestContext(request) )

def setlist(request):
    return render_to_response( 'setlist.html', context_instance=RequestContext(request) )
