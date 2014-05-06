from rest_framework import viewsets
from app_drf.models import AppDrfModel
from .serializers import AppDrfModelSerializer
# Create your views here.

class AppDrfModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AppDrfModel.objects.all()
    serializer_class = AppDrfModelSerializer
