from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
  
    # homepage routes
    url( r'^$', 			'apps.home.views.index',  name='home' ),
    url( r'^logout$',       'apps.home.views.index',  name='logout' ),


    #users routes
    url( r'^users/$', 	 	'apps.users.views.index', 	name='home' ),
    url( r'^users/new$', 	'apps.users.views.new', 	name='home' ),
    url( r'^users/login$', 	'apps.users.views.login', 	name='home' ),
    url( r'^dashboard/$',   'apps.users.views.dashboard',   name='bands' ),

    #bands routes
    url( r'^bands/$',       'apps.bands.views.show_bands',  name='show_bands' ),
   
    # event routes
    url( r'^events/$',      'apps.events.views.events',  name='home' ),

    # setlist routes
    url( r'^setlist/$',     'apps.setlists.views.setlist',  name='setlist' ),

    #login routes
    url( r'^users/$', 		'apps.login.urls',  name='home' ),

    # basically hacks for now... need to clean up
    url( r'^about/$', 		'apps.users.views.about',  name='home' ),

    # admin routes
    #url( r'^admin/doc/', include('django.contrib.admindocs.urls') ),
    #url( r'^admin/', 	include(admin.site.urls) ),
)
