from django.db import models

# Create your models here.

class AppDrfModel(models.Model):
    name = models.CharField(max_length=200)
    appFlag = models.BooleanField(default=True)
    appFlagTwo = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

from django.core.urlresolvers import resolve
from django.core.urlresolvers import reverse

class VersionSwitch(object):

    def process_request(self, request):
        r = resolve(request.path_info)
        version = request.META.get('HTTP_X_VERSION', False)
        if r.namespace.startswith('app_drf:') and version:
            old_version = r.namespace.split(':')[-1]
            request.path_info = reverse('{}:{}'.format(r.namespace.replace(old_version, version), r.url_name), args=r.args, kwargs=r.kwargs)