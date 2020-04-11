from django.urls import path,include
from .views import *


urlpatterns = [
    path('',HomeList.as_view(),name='home'),
]


