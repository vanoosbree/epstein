from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import login, logout

# don't really need these two
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
  
    # homepage routes
    url( r'^$', 			'apps.home.views.index',  name='home' ),
    url( r'^about/$',       'apps.home.views.about',  name='about' ),

    #users routes
    url( r'^users/$', 	 	'apps.users.views.index', 	name='home' ),
    url( r'^users/new$', 	'apps.users.views.new', 	name='home' ),
    url( r'^users/create$', 'apps.users.views.create',     name='home' ),
    url( r'^users/login$', 	'apps.users.views.do_login', 	name='home' ),
    url( r'^users/logout$', 'apps.users.views.do_logout',    name='home' ),
    url( r'^dashboard/$',   'apps.users.views.dashboard',   name='bands' ),

    #bands routes
    url( r'^bands/create$',         'apps.bands.views.create',  name='show_bands' ),
    url( r'^bands/(\d+)/$',         'apps.bands.views.dashboard',  name='band dashboard' ),
    url( r'^bands/(\d+)/join/$',    'apps.bands.views.join',  name='show_bands' ),
    url( r'^bands/(\d+)/leave/$',   'apps.bands.views.leave',  name='show_bands' ),

    # event and set list routes
    url( r'^bands/(\d+)/events/(\d+)/$',        'apps.events.views.show',  name='show_event' ),
    url( r'^bands/(\d+)/events/(\d+)/setlist/$','apps.setlists.views.setlist',  name='setlist' ),
    url( r'^bands/(\d+)/events/create/$',       'apps.events.views.create',  name='setlist' ),
    url( r'^bands/(\d+)/events/(\d+)/edit/$',   'apps.events.views.edit',  name='setlist' ),
    url( r'^bands/(\d+)/events/(\d+)/update/$', 'apps.events.views.update',  name='setlist' ),
    
    # songs routes
    url( r'^bands/(\d+)/songs/$',           'apps.songs.views.index',      name='show_songs' ),
    url( r'^bands/(\d+)/songs/create/$',    'apps.songs.views.create',     name='create_song' ),
    url( r'^bands/(\d+)/songs/(\d+)/edit/$', 'apps.songs.views.edit_page',  name='edit_song_page' ),
    url( r'^bands/(\d+)/songs/(\d+)/update/$', 'apps.songs.views.update',     name='modify song data' ),
    url( r'^bands/(\d+)/songs/(\d+)/delete/$', 'apps.songs.views.delete',     name='modify song data' ),

    url( r'^bands/(\d+)/events/(\d+)/setlist/$', 'apps.setlists.views.index',     name='show set list' ),
    url( r'^bands/(\d+)/events/(\d+)/setlist/update/$', 'apps.setlists.views.update',     name='show set list' ),

    # admin routes
    #url( r'^admin/doc/', include('django.contrib.admindocs.urls') ),
    #url( r'^admin/', 	include(admin.site.urls) ),
)
