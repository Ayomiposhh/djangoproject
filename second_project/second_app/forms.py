from dataclasses import fields
from email import message
from pyexpat import model
# from pyexpat import model
# from socket import fromshare
# from unicodedata import name
from django import forms
from second_app.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.core import validators





class ContactForm(forms.ModelForm):
    name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Name'}))
    email = forms.EmailField(label='Email :', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
    message =forms.CharField(label='Message :', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    
    class Meta():
     model=Contacts
     fields= ['name', 'email', 'message']
    


    
class BlogForm(forms.ModelForm):
    title = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Blog Title'}))
    slug = forms.SlugField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Slug Title'}))
    image= forms.ImageField(label='Add Image :', widget=forms.FileInput(attrs={'class': 'form-control', }))
    content=forms.CharField(label='Message :', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    
    class Meta():
     model= Post
     fields= ['user','slug','title','image','content']  
     


# class RegForm(UserCreationForm):
#   class Meta():
#    model= User
#    fields= ('username','first_name','last_name','email')

class RegForm(UserCreationForm):
    username = forms.CharField(label='Username :', widget=forms.TextInput(
        attrs={'class': 'input-text', 'placeholder': 'Enter Username'}))
    email = forms.EmailField(label='Email :', widget=forms.EmailInput(attrs={'class': 'input-text', 'placeholder': 'Enter Email'}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'input-text', 'placeholder': 'Enter Firstname'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'input-text', 'placeholder': 'Enter Lastname'}))
    password1 = forms.CharField(label='Enter Password :', widget=forms.PasswordInput(
        attrs={'class': 'input-text', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'input-text', 'placeholder': 'Enter Password'}))
    botfield = forms.CharField(required=False, widget=forms.HiddenInput(),
                               validators=[validators.MaxLengthValidator(0)])

    def clean_email(self):
        email_field = self.cleaned_data.get('email')
        if User.objects.filter(email=email_field).exists():
            raise forms.ValidationError('Email already exist')
        return email_field

    class Meta():
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']
        
class EditForm(UserChangeForm):
    username = forms.CharField(label='Username :', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
    email = forms.EmailField(label='Email :', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Firstname'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Lastname'}))
    botfield = forms.CharField(required=False, widget=forms.HiddenInput(),
                               validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', ]


class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old password', widget=forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder':'Enter Password'}))
    new_password1 = forms.CharField(label='New password', widget=forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder':'Enter Password'}))
    new_password2= forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder':'Enter Password'}))

    botfield = forms.CharField(required=False, widget=forms.HiddenInput(),
                               validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = User
        fields = ['password1', 'password2']

      

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']
        
        if commit:
            user.save()
            return user       
        
        
class UserForm(forms.ModelForm):
    number = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Number'}))
    image= forms.ImageField( required=False, label='Add Image :', widget=forms.FileInput(attrs={'class': 'form-control', }))
    address =forms.CharField( required=False, label='Address :', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Address'}))
    website =forms.URLField( required = False, label=' Enter Website:', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'HTTPS'}))
    
    
    class Meta():
     model= UserProfile
     fields= ['image','number','address','website']  

     
class CommentForm(forms.ModelForm):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}))
    email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
    body=forms.CharField(label='Message :', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        
        
        
class EditBlogForm(forms.ModelForm):
    title = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Blog Title'}))
    slug = forms.SlugField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Slug Title'}))
    image= forms.ImageField(label='Add Image :', widget=forms.FileInput(attrs={'class': 'form-control', }))
    content=forms.CharField(label='Message :', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    
    class Meta():
     model= Post
     fields= ['user','slug','title','image','content']  
     