from django.conf.urls import patterns, include, url

#from app_drf import views
#from rest_framework import routers
from django.conf.urls import *

import app_drf.v2.urls as v2_urls
import app_drf.v1.urls as v1_urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test_drf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^v2/', include('app_drf.v2.urls', namespace='v2')),
    url(r'^v1/', include(v1_urls, namespace='v1')),
#    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

