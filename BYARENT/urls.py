from django.urls import path,include
from .views import *
from . import views


urlpatterns = [
    path('',HomeList.as_view(),name='home'),
    path('register',views.registerpage,name='register'),
    path('login',views.loginpage,name='login'),
    # path('register',RegisterList.as_view(),name='register'),
    path('rent', views.RentList,name='rent'),



]


