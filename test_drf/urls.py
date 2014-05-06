from django.conf.urls import patterns, include, url

from django.contrib import admin

#from test_drf.app_drf import *

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'test_drf.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       #    url(r'^', include(router.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^app_drf/', include('app_drf.urls', namespace='app_drf'))
)
