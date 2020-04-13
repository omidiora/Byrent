from django.shortcuts import render,redirect
from django.views.generic import ListView
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.

class HomeList(ListView):
    model=Home
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['homes'] = Home.objects.all()
        print('homes')
        return context
    


def registerpage(request):
    form=CustomUserCreationForm()
    if request.method== 'POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'forms':form}
            
    return render(request,'register.html',context)

def loginpage(request):
    form=CustomUserCreationForm()
    if request.method =='POST':
         username=request.POST.get('username')
         password=request.POST.get('password')
         user=authenticate(request,username=username,password=password)
         if user is not None:
             login(request,user)
             return redirect('/')
         else:
            return  render(request,'login.html')
    context={'form':form}
    return  render(request,'login.html',context)
    
            

class RentList(ListView):
    model=Home
    template_name='rent.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['homes'] = Home.objects.all()
        print('homes')
        return context



         
