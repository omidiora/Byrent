from rest_framework import serializers
from BYARENT.models import Home


class HomeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Home
        fields=['name','image','price','description']