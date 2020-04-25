from rest_framework import generics
from BYARENT.models import *
from .serializers import  HomeModelSerializer

class  HomeModelSerializer(generics.ListAPIView):
    serializer_class= HomeModelSerializer
    
    def get_queryset(self):
        return Home.objects.all()