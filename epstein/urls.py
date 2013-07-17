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
    url( r'^bands/(\d+)/events/(\d+)/$',  'apps.events.views.show',  name='show_event' ),
    url( r'^bands/(\d+)/events/(\d+)/setlist/$',     'apps.setlists.views.setlist',  name='setlist' ),

    # defunct routes
    #url( r'^bands/$',       'apps.bands.views.show_bands',  name='show_bands' ),
    #url( r'^band/$',        'apps.bands.views.dashboard',  name='show_bands' ),
    #url( r'^events/$',      'apps.events.views.events',  name='home' ),

    # admin routes
    #url( r'^admin/doc/', include('django.contrib.admindocs.urls') ),
    #url( r'^admin/', 	include(admin.site.urls) ),
)
