from rest_framework import serializers

from app.models import *
class LaptopsMS(serializers.ModelSerializer):
    class Meta:
        model=Laptops
        fields="__all__"