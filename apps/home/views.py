# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

import datetime

def index(request):
    #html = "<html><body><h1>This is the polls, beeyotch!</h1></body></html>"
    #return HttpResponse(html)
    # data = {
    #     'name' : 'John',
    #     'email': 'johnholloway79@gmail.com'
    # }
    return render_to_response( 'home.html', context_instance=RequestContext(request) )

def home(request):
    data = {
        'name' : 'John',
        'email': 'johnholloway79@gmail.com'
    }
    return render_to_response( 'index.html', data, context_instance=RequestContext(request) )

def something(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def logout(request):
    return render_to_response( 'home.html', data, context_instance=RequestContext(request) )
