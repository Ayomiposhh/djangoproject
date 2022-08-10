from email import message
from pickle import TRUE
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
  
  
STATUS =(
  (0, "Draft"),
  (1,"Publish")
)


class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=150,null=True, blank=True)
    slug=models.SlugField(null=True)
    email=models.EmailField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField()
    created_on =models.DateTimeField(auto_now_add=True)
    content =HTMLField()
  

  
    class Meta:
      ordering =[ '-created_on']
      
      
    def __str__(self):
     return self.title                                    
                                                                     
                                      
class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=100, blank=True)
  last_name = models.CharField(max_length=100, blank=True)
  email = models.EmailField(max_length=150)
  image = models.ImageField(blank=True, null=True, help_text='Dimension 600px X 671px')
  number = models.CharField(max_length= 15,null=True,blank=True) 
  website = models.URLField(blank=True, null=True) 
  address=models.CharField(max_length= 1000,null=True,blank=True)
  # your_cv = models.FileField(blank=True, null=True,upload_to='uploads/pdf')
  def __str__(self):  
   return self.user.username
 
  def get_profile_img(self):
        if self.image:
            return self.image.url



def create_profile(sender, instance, created, *args, **kwargs):
    # ignore if this is an existing User
    if not created:
        return
    UserProfile.objects.create(user=instance)
post_save.connect(create_profile, sender=User)

class Contacts(models.Model):
  name= models.CharField(max_length= 100,null=True,blank=True)
  email=models.EmailField()
  message=models.TextField()

  def __str__(self): 
    return self.name


class Education(models.Model):
  title = models.CharField(max_length= 200,null=True,blank=True)
  name =models.CharField(max_length= 200,null=True,blank=True)
  year = models.CharField(max_length= 100,null=True,blank=True)
  course =models.CharField(max_length= 100,null=True,blank=True)
 
  def __str__(self): 
    return self.title
  
class Experience(models.Model):
  title = models.CharField(max_length= 500,null=True,blank=True)
  year = models.CharField(max_length= 100,null=True,blank=True)
  company = models.CharField(max_length= 1000,null=True,blank=True)
  text =HTMLField(max_length= 1000,null=True,blank=True)
 
  def __str__(self): 
    return self.title
  
  
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
  