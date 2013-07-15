# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def events(request):
    return render_to_response( 'events/events.html', context_instance=RequestContext(request) )
