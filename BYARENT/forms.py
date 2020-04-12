from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from .models import *

class HomeForm(forms.ModelForm):
     name=forms.CharField(label='',widget=forms.TextInput(attrs={'class':"form-control"}))
     price=forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder':"YOUR MESSAGE",'class':"form-control"}))
     description=forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder':"YOUR MESSAGE",'class':"form-control"}))
    
     class Meta:
        model=Home
        fields=['name','description','price']
    
    
class CustomUserCreationForm(forms.Form):
    use_required_attribute = False
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150,widget=forms.TextInput(attrs={'class':"form-control",'required':'False'}),)
    email = forms.EmailField(label='Enter email',widget=forms.TextInput(attrs={'class':"form-control"}))
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput(attrs={'class':"form-control",'required':'False'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class':"form-control",'required':'False'}))
 
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username
 
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email
 
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
 
        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
 
        return password2
 
    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user
      
   
