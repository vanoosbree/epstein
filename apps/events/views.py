# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def events(request):
    events = {}
    view_data = { 'band' : 'Seamen Vaccum', 'events' : events }
    return render_to_response( 'events/events.html', view_data, context_instance=RequestContext(request) )
