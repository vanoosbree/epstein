# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.bands.models import Band, UserHasBand

def show_bands(request):
    return render_to_response( 'bands/bands.html', context_instance=RequestContext(request) )

def dashboard(request, id):
    events = {}
    cur_band 	= Band.objects.get(pk=id)
    view_data = { 'band' : cur_band.name, 'events' : events }
    return render_to_response( 'bands/dashboard.html', view_data, context_instance=RequestContext(request) )

def join(request, band_id):
    this_user 	= request.user
    this_band 	= Band.objects.get(pk=band_id)
    membership 	= UserHasBand( user=this_user, band=this_band )
    membership.save()
    return render_to_response( 'users/dashboard.html', context_instance=RequestContext(request) )	

def leave(request, band_id):
    this_user 	= request.user
    this_band 	= Band.objects.get(pk=band_id)

    membership = UserHasBand.objects.get( user_id=this_user.id, band_id=this_band.id)
    membership.delete()
    return render_to_response( 'users/dashboard.html', context_instance=RequestContext(request) )	

def create(request):
    this_user 	= request.user
    band_name 	= request.POST.get( 'band_name', '' )
    this_band 	= Band.objects.create( name=band_name ) 
    membership 	= UserHasBand( user=this_user, band=this_band )
    membership.save()
    return render_to_response( 'users/dashboard.html', context_instance=RequestContext(request) )	

def delete_band(request):
	return render_to_response( 'users/dashboard.html', context_instance=RequestContext(request) )	