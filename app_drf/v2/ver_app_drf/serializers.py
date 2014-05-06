from rest_framework import serializers
from app_drf.models import AppDrfModel


class AppDrfModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppDrfModel
        fields = ('name', 'appFlag', 'appFlagTwo')

