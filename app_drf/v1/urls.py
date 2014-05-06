from django.conf.urls import patterns, include, url

from django.conf.urls import *
from .ver_app_drf import views as ver_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'^', ver_views.AppDrfModelViewSet)

urlpatterns = router.urls

#    patterns('',
    # Examples:
    # url(r'^$', 'test_drf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^admin/', include(admin.site.urls)),
#    url(r'', include('test_drf.app_drf.v2.urls', namespace='default')),
#    url(r'^v1/', include('test_drf.app_drf.v1.urls', namespace='v1')),
#    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
#)
