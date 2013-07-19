from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.bands.models import Band, UserHasBand
from apps.events.models import Event
#import datetime if not broken on July 24th, delete!

def show_bands(request):
    return render_to_response( 'bands/bands.html', context_instance=RequestContext(request) )

def dashboard(request, id):
    cur_band 	= Band.objects.get(pk=id)
    events		= Event.objects.filter(band_id=id).order_by( 'date' )
    view_data 	= { 'band' : cur_band, 'events' : events }
    return render_to_response( 'bands/dashboard.html', view_data, context_instance=RequestContext(request) )

def list(request):
    bands   = Band.objects.get()
  
  
    return HttpResponseRedirect('/dashboard/')

def join(request, band_id):
    this_user 	= request.user
    this_band 	= Band.objects.get(pk=band_id)
    membership 	= UserHasBand( user=this_user, band=this_band )
    membership.save()
    return HttpResponseRedirect('/dashboard/')

def leave(request, band_id):
    this_user 	= request.user
    this_band 	= Band.objects.get(pk=band_id)

    membership = UserHasBand.objects.get( user_id=this_user.id, band_id=this_band.id)
    membership.delete()
    return HttpResponseRedirect('/dashboard/')

def create(request):
    this_user 	= request.user
    band_name 	= request.POST.get( 'band_name', '' )
    this_band 	= Band.objects.create( name=band_name ) 
    membership 	= UserHasBand( user=this_user, band=this_band )
    membership.save()
    return HttpResponseRedirect('/dashboard/')
  
def delete_band(request):
    return HttpResponseRedirect('/dashboard/')