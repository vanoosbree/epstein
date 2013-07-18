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
    setlist = Setlist.objects.get(event_id=eventid)

    song_order = []

    if setlist.songs:
        song_order = setlist.songs.split(',')

        for i in range(0, len(song_order)):
    	    song_order[i] = int( song_order[i] )

    songs_avail  = Song.objects.filter(band_id=bandid).exclude(id__in=song_order)
    #songs_in_set = Song.objects.filter(band_id=bandid, pk__in=song_order)
    songs_in_set = Song.objects.in_bulk(song_order)
    sorted_songs = [songs_in_set[id] for id in song_order]

    view_data = { 'event' : event, 'band' : band, 'songs_avail' : songs_avail, 'songs_in_set' : sorted_songs }
    return render_to_response( 'setlists/setlist.html', view_data, context_instance=RequestContext(request) )

def update(request,bandid,eventid):
    event 	= Event.objects.get(pk=eventid)
    band  	= Band.objects.get(pk=bandid)
    setlist = Setlist.objects.get(event_id=eventid)
    songs 	= Song.objects.filter(band_id=bandid)
    sort1 =  request.POST.getlist( 'sort1' )
    sort2 =  request.POST.getlist( 'sort2' )
    order = '-'.join(sort2)
    setlist.songs = order
    setlist.save()
    view_data = { 'event' : event, 'band' : band, 'songs' : songs }
    return render_to_response( 'setlists/setlist.html', view_data, context_instance=RequestContext(request) )