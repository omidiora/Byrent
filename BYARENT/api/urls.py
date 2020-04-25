from django.urls import path,include
from BYARENT.api.views import *


urlpatterns = [
   
    
    path('', HomeModelSerializer.as_view(),name='home')



]


