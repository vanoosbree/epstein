from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
  
    # homepage routes
    url( r'^$', 			'apps.home.views.index',  name='home' ),
    url( r'^home/$', 		'apps.home.views.home',   name='home' ),

    #users routes
    url( r'^users/$', 	 	'apps.users.views.index', 	name='home' ),
    url( r'^users/new$', 	'apps.users.views.new', 	name='home' ),
    url( r'^users/login$', 	'apps.users.views.login', 	name='home' ),

    #bands routes
    url( r'^dashboard/$', 	 'apps.users.views.dashboard', 	name='bands' ),


    #login routes
    url( r'^users/$', 		'apps.login.urls',  name='home' ),

    # basically hacks for now... need to clean up
    url( r'^about/$', 		'apps.users.views.about',  name='home' ),
    url( r'^bands/$', 		'apps.users.views.bands',  name='home' ),
    url( r'^events/$', 		'apps.users.views.events',  name='home' ),
    url( r'^setlist/$', 	'apps.users.views.setlist',  name='home' ),

    # admin routes
    #url( r'^admin/doc/', include('django.contrib.admindocs.urls') ),
    #url( r'^admin/', 	include(admin.site.urls) ),
)
