# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import datetime
from django.contrib import auth
from django.contrib.auth.models import User

def index(request):
    my_data = {}
    return render_to_response( 'users/index.html', my_data, context_instance=RequestContext(request) )

def login(request):
    now = datetime.datetime.now()
    my_data = {}
    return render_to_response( 'users/login.html', my_data, context_instance=RequestContext(request) )

def new(request):
    my_data = {}
    return render_to_response( 'users/new.html', my_data, context_instance=RequestContext(request) )

def create(request):
    first_name = request.POST.get( 'first_name', '' )
    last_name = request.POST.get( 'last_name', '' )
    email_addr = request.POST.get( 'last_name', '' )
    password = request.POST.get( 'last_name', '' )
    password_confirm = request.POST.get( 'password_confirm', '' )
    #user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    my_data = {}
    return render_to_response( 'users/index.html', my_data, context_instance=RequestContext(request) )

def do_login(request):
    email_addr = request.POST.get( 'last_name', '' )
    password = request.POST.get( 'last_name', '' )

def about(request):
    return render_to_response( 'about.html', context_instance=RequestContext(request) )

def bands(request):
    return render_to_response( 'bands.html', context_instance=RequestContext(request) )

def events(request):
    return render_to_response( 'events.html', context_instance=RequestContext(request) )

def setlist(request):
    return render_to_response( 'setlist.html', context_instance=RequestContext(request) )

def dashboard(request):
    return render_to_response( 'users/dashboard.html', context_instance=RequestContext(request) )
