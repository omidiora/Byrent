from django.shortcuts import render
from django.views.generic import ListView
from .models import *


# Create your views here.

class HomeList(ListView):
    model=Home
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['homes'] = Home.objects.all()
        print('homes')
        return context



    
