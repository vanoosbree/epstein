# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def show_bands(request):
    return render_to_response( 'bands/bands.html', context_instance=RequestContext(request) )

def dashboard(request):
    events = {}
    view_data = { 'band' : 'Seamen Vaccum', 'events' : events }
    return render_to_response( 'bands/dashboard.html', view_data, context_instance=RequestContext(request) )
