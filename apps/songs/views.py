from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from apps.bands.models import Band
from apps.songs.models import Song

def index(request,bandid):
    my_band = Band.objects.get(pk=bandid)
    songs = Song.objects.filter(band_id=bandid)
    my_data = { 'band' : my_band , 'songs' : songs}
    return render_to_response( 'songs/index.html', my_data, context_instance=RequestContext(request) )

def edit_page(request,bandid,songid):
    my_band = Band.objects.get(pk=bandid)
    song = Song.objects.get(pk=songid)
    my_data = { 'band' : my_band , 'song' : song}
    return render_to_response( 'songs/edit.html', my_data, context_instance=RequestContext(request) )

def update(request,bandid,songid):
    new_title 		= request.POST.get( 'title', '')
    new_desc		= request.POST.get( 'description', '' )
    song			= Song.objects.get(pk=songid)
    song.title 		= new_title
    song.description= new_desc
    song.save()
    url = "/bands/%s/songs" % bandid
    return HttpResponseRedirect( url )

def create(request, bandid):
    this_user 		= request.user
    new_title 		= request.POST.get( 'title', '')
    new_desc		= request.POST.get( 'description', '' )
    origin			= request.POST.get( 'origin', '' )
    event_id		= request.POST.get( 'event_id', '' )
    song 			= Song.objects.create(band_id=bandid, title=new_title, description=new_desc)
    song.save()

    if origin == 'songs':
        url = "/bands/%s/songs" % bandid
    else:
        url = "/bands/%s/events/%s/setlist" % (bandid, event_id)
        
    return HttpResponseRedirect( url )

def delete(request,bandid,songid):
    song			= Song.objects.get(pk=songid)
    song.delete()
    url = "/bands/%s/songs" % bandid
    return HttpResponseRedirect( url )