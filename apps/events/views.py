from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.bands.models import Band
from apps.events.models import Event 
from apps.setlists.models import Setlist

def show(request, bandid, eventid):
    events = {}
    cur_band = Band.objects.get(pk=bandid)
    event = Event.objects.get(pk=eventid)
    messages = [ { 'user': 'John', 'message' : 'I am a ninja' }, { 'user': 'Singer', 'message' : 'I need drugs!' } ]
   
    view_data = { 'band' : cur_band, 'event' : event, 'messages' : messages }
    return render_to_response( 'events/event.html', view_data, context_instance=RequestContext(request) )

def edit(request, bandid, eventid):
    cur_band    = Band.objects.get(pk=bandid)
    event       = Event.objects.get(pk=eventid)   
    view_data = { 'band' : cur_band, 'event' : event }
    return render_to_response( 'events/edit.html', view_data, context_instance=RequestContext(request) )

def update(request, bandid, eventid):
    cur_band            = Band.objects.get(pk=bandid)
    event               = Event.objects.get(pk=eventid)
    event.date          = request.POST.get( 'date', '' )
    event.time          = request.POST.get( 'time', '' )
    event.description   = request.POST.get( 'description', '' )
    event.address       = request.POST.get( 'address', '' )
    event.save()
   
    url = "/bands/%s/events/%s/" % (bandid, eventid)
    return HttpResponseRedirect( url )

def create(request, bandid):
    this_user 	= request.user
    new_date 		= request.POST.get( 'date', '' )
    new_time		= request.POST.get( 'time', '' )
    new_desc		= request.POST.get( 'description', '' )
    new_address		= request.POST.get( 'address', '' )
    event 		= Event.objects.create(venue_id=0, band_id=bandid, date=new_date, time=new_time, description=new_desc, address=new_address)
    event.save()

    setlist      = Setlist.objects.create(event_id=event.id)
    setlist.save()

    url = "/bands/%s/" % bandid
    return HttpResponseRedirect( url )
