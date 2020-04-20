from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .filters import HomeFilter

# Create your views here.

class HomeList(ListView):
    model=Home
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['homes'] = Home.objects.all()[0:6]
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
    


def  RentList(request):
    home=Home.objects.all()
    myfilter=HomeFilter(request.GET,queryset=Home.objects.all())
    print(myfilter)
    orders=myfilter.qs
    print(orders)
    context={'myfilter':myfilter,'orders':orders,'home':home}
    return render(request,'rent.html',context)




class ContactDetailView(DetailView):
    template_name='contact.html' 

















    


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



