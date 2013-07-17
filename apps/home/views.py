from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    view_data = { 'user': request.user }
    return render_to_response( 'home.html', view_data, context_instance=RequestContext(request) )

def about(request):
    return render_to_response( 'about.html', context_instance=RequestContext(request) )

def contact(request):
    return render_to_response( 'contact.html', context_instance=RequestContext(request) )