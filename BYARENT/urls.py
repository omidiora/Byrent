from django.urls import path,include
from .views import *
from . import views


urlpatterns = [
    path('',HomeList.as_view(),name='home'),
    # path('register',views.registerpage,name='register'),
    path('login',views.loginpage,name='login'),
    path('rent', RentListView.as_view(),name='rent'),
    path('contact/', contactView, name='contact'),
    



]


