import django_filters
from .models import *


class HomeFilter(django_filters.FilterSet):
    class Meta:
        model = Home
        fields =['name']
       
        
        
