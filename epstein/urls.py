from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
  
    # homepage routes
    url( r'^$', 			'apps.home.views.index',  name='home' ),
    url( r'^home/$', 		'apps.home.views.home',   name='home' ),

    #users routes
    url( r'^users/$', 	 	'apps.users.views.index', 	name='user index' ),
    url( r'^users/register$', 	'apps.users.views.new', 	name='new user' ),
    url( r'^users/login$', 	'apps.users.views.login', 	name='user login' ),
    url( r'^users/create$', 'apps.users.views.create', 	name='create user' ),

    #bands routes
    url( r'^dashboard/$', 	 'apps.users.views.dashboard', 	name='user dashboard' ),


    # do da login
    #url( r'^user/$',       include( 'apps.login.urls'),  name='user login/registration' ),
    url( r'^register$',     'apps.login.views.register', name='user register' ),
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
