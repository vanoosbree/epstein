from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

urlpatterns = patterns( 'apps.login.views',

    url( r'^register$', 'register', name='user register' ),
    url( r'^login$', 	'login', 	name='user login' ),
    url( r'^logout$', 	'logout', 	name='user logout' ),
)

urlpatterns += patterns('',
	url( r'^$', 'login', kwargs={'template_name':'login/index.html'}, name='user login' ),
	url( r'^logout$', 'logout', kwargs={'next_page':'/'}, name='user logout' ),
)


