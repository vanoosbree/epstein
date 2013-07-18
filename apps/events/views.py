# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.bands.models import Band
from apps.events.models import Event 

def show(request, bandid, event_id):
    events = {}
    cur_band = Band.objects.get(pk=bandid)
    events = Event.objects.filter(band_id=bandid)
   
    view_data = { 'band' : cur_band.name, 'events' : events }
    return render_to_response( 'events/event.html', view_data, context_instance=RequestContext(request) )


def create(request, bandid):
    this_user 	= request.user
    #new_date = time.strftime("%Y%m%d", request.POST.get( 'date', '' ))
    new_date 		= request.POST.get( 'date', '' )
    new_time		= request.POST.get( 'time', '' )
    new_desc		= request.POST.get( 'description', '' )
    new_address		= request.POST.get( 'address', '' )
    event 		= Event.objects.create(venue_id=0, band_id=bandid, date=new_date, time=new_time, description=new_desc, address=new_address)
    event.save()
    #url = '/bands/%s' % bandid
    #HttpResponseRedirect( url )
    return render_to_response( 'users/dashboard.html', context_instance=RequestContext(request) )	
