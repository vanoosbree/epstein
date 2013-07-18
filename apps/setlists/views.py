# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.bands.models import Band
from apps.songs.models import Song
from apps.events.models import Event
from apps.setlists.models import Setlist

def setlist(request,bandid,eventid):
    event = Event.objects.get(pk=eventid)
    band  = Band.objects.get(pk=bandid)
    songs = Song.objects.filter(band_id=bandid)

    view_data = { 'event' : event, 'band' : band, 'songs' : songs }
    return render_to_response( 'setlists/setlist.html', view_data, context_instance=RequestContext(request) )

def update(request,bandid,eventid):
    event = Event.objects.get(pk=eventid)
    band  = Band.objects.get(pk=bandid)
    songs = Song.objects.filter(band_id=bandid)

    sort1 =  request.POST.getlist( 'sort1' )
    sort2 =  request.POST.getlist( 'sort2' )

    order = '-'.join(sort2)

    print "order: ", order

    #setlist = Setlist.objects.create(event_id=eventid, songs=sort2 )
    #setlist.save()

    view_data = { 'event' : event, 'band' : band, 'songs' : songs }
    return render_to_response( 'setlists/setlist.html', view_data, context_instance=RequestContext(request) )