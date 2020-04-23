from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .filters import HomeFilter
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from .decorators import  unauthenticated_user

# Create your views here.

class HomeList(ListView):
    model=Home
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['homes'] = Home.objects.all()[0:6]
        return context
    


# def registerpage(request):
#     form=CustomUserCreationForm()
#     if request.method== 'POST':
#         form=CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     context={'forms':form}
            
#     return render(request,'register.html',context)

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
    


def  RentList(request):
    home=Home.objects.all()
    myfilter=HomeFilter(request.GET,queryset=Home.objects.all())

    orders=myfilter.qs

    context={'myfilter':myfilter,'orders':orders,'home':home}
    return render(request,'rent.html',context)

class RentListView(ListView):
    template_name='rent.html'
    def get_queryset(self,*args,**kwargs):
        qs=Home.objects.all()
        query=self.request.GET.get("q",None)
        if query is not None:
            qs=qs.filter(Q(name__icontains=query))
            print(qs)
        return qs
  
    def get_context_data(self,*args,**kwargs):
        context=super(RentListView,self).get_context_data(*args,**kwargs)
        context['orders']=Home.objects.all()
        return context
    


      




def contactView(request):
    form=ContactForm()
    if request.method =='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(subject,message,from_email,['omidioraemmanuel@gmail.com'])
            return redirect('/')
    context={'form':form}
    return render(request,'contact.html',context)

        
















    


# class RentList(ListView):
#     model=Home
#     template_name='rent.html'
#     home=Home.objects.all() 
    
    

#     def get_context_data(self, **kwargs):
#         context = super(RentList,self).get_context_data(**kwargs)
#         myhome=HomeFilter(request.GET,queryset=Home)
#         myhomefilter=myhome.qs
#         context['homes'] = Home.objects.all()
#         context['myfilter']=myhomefilter
#         print('homes')
#         return context



