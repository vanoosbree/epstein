# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def setlist(request):
    return render_to_response( 'setlists/setlist.html', context_instance=RequestContext(request) )
