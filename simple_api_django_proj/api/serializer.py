from rest_framework import serializers
from .models import *
class TestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=TaskModel
        fields="__all__"