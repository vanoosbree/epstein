# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.bands.models import Band
from apps.events.models import Event 

def show(request, band_id, event_id):
    events = {}
    cur_band = Band.objects.get(pk=band_id)
    #event = Event.objects.get(pk=event_id)
    view_data = { 'band' : cur_band.name, 'events' : events }
    return render_to_response( 'events/event.html', view_data, context_instance=RequestContext(request) )
