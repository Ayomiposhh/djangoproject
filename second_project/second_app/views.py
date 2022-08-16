from email import message
import profile
from django.shortcuts import render,redirect
from django.http import HttpResponse
from second_app.forms import *
from django.contrib.auth.models import User
from django.db import IntegrityError
from second_app.models import Post,User
from django.contrib import messages
from django.views.generic import CreateView,UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, get_object_or_404
# from. models import Blog


# Create your views here.

class BlogList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name= 'second_app/blog.html'
    context_object_name= 'blog_list'
    
# class BlogDetail(generic.DetailView):
#     model=Post
#     template_name= 'second_app/blog-single.html'
#     context_object_name= 'blog_detail'
  

def home(request):
  blog = Post.objects.filter(status=1).order_by('-created_on')[:3]
  edu = Education.objects.all()
  exp = Experience.objects.all()
  wrk = Work.objects.all()
  skl = Skill.objects.all()
  if request.method =='POST':
    contact_form = ContactForm(request.POST)
    if contact_form.is_valid():
      contact_form.save()   
  else:
    contact_form = ContactForm()
  return render(request,'second_app/index.html',{'blog':blog, 'cform':contact_form, 'edu': edu, 'exp' : exp, 'wrk':wrk,'skl': skl})


def register(request):
  if request.method == 'POST':
    register_form=RegForm(request.POST, request.FILES)
    if register_form.is_valid():
      user = register_form.save()
      user.refresh_from_db()
      user.userprofile.first_name = register_form.cleaned_data.get('first_name')
      user.userprofile.last_name = register_form.cleaned_data.get('last_name')
      user.userprofile.email = register_form.cleaned_data.get('email')
      user.userprofile.phone = register_form.cleaned_data.get('phone')
      register_form.save()
      messages.success(request,'You have been registered')
    # return redirect('second_app:login')
    
  else:
       register_form=RegForm()
       messages.error(request,'Password must contain lowercases and character')
  return render(request,'second_app/register.html',{'reg': register_form})
  
  
def edit(request):
  if request.method == 'POST':
    edit=EditForm(request.POST, instance=request.user)
    user_pro = UserForm(request.POST,request.FILES,instance=request.user.userprofile)
    
    if edit.is_valid() and user_pro.is_valid():
      edit.save()
      user_pro.save()
      messages.success(request,'User edited successfully')
    
  else:
    edit=EditForm(instance=request.user)
    user_pro = UserForm(instance=request.user.userprofile)
  return render(request,'dashboard/edit.html',{'edit_key':edit, 'up': user_pro})
  
def pass_change(request):
  if request.method == 'POST':
    edit_pass = PasswordChangeForm(data=request.POST, user=request.user)
    if edit_pass.is_valid():
      edit_pass.save()
      update_session_auth_hash(request,edit_pass.user)
      messages.success(request,'Password Changed Successfully')
    
  else:
     edit_pass = PasswordChangeForm(user=request.user)
  return render(request,'dashboard/edit_pass.html',{'pass_key': edit_pass})


class Addblog(SuccessMessageMixin,CreateView):
  model =Post
  template_name ='dashboard/form.html'
  form_class =BlogForm
  success_url= reverse_lazy('second_app:add_blog')
  success_message = 'Post Added Successfully'
  
  
# class UpdateBlog(SuccessMessageMixin,UpdateView):
#   model =Post
#   template_name ='dashboard/form.html'
#   form_class =BlogForm
#   success_url= reverse_lazy('second_app:update_blog')
#   success_message = 'Update Successfully'
  
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('second_app:dashboard')
        else:
            messages.error(request, 'Username and Password do not match')
    return render(request, 'second_app/login.html')
  
# class DeleteBlog(generic.DeleteView):
#   model =Post
#   template_name ='dashboard/viewblog.html'
#   success_url= reverse_lazy('second_app:view_blog')


def delete_post(request,post_id):
    post_record = get_object_or_404(Post,id=post_id)
    post_record.delete()
    return redirect('second_app:view_blog')
  
def logout_view(request):
       logout(request)
       return redirect('second_app:login')
  
  
def dashboard(request):
   return render(request,'dashboard/index.html')
 

def viewprofile(request):
  pro= UserProfile.objects.filter(user=request.user)
  return render(request, 'dashboard/view_profile.html',{'pro' : pro,})



def post_detail(request, slug):
    template_name= 'second_app/blog-single.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'blog_detail': post,'comments': comments,'new_comment': new_comment,'comment_form': comment_form})
  
  
def viewblog(request):
  view_blog=Post.objects.filter(user=request.user)
  return render(request, 'dashboard/viewblog.html',{'view_blog' : view_blog,})


def viewdetail(request,post_id):
  view_detail=Post.objects.filter(user=request.user,id=post_id)
  return render(request, 'dashboard/viewdetail.html',{'view_detail' : view_detail,})
    
    
    
def updateblog(request,post_id):
  edit_blog=get_object_or_404(Post,id=post_id)
  if request.method == 'POST':
    edit_blog_form = EditBlogForm(request.POST,request.FILES, instance=  edit_blog)
    if edit_blog_form.is_valid():
      edit_blog_form.save()
      messages.success(request,'Update Successfully')
    
  else:
     edit_blog_form = EditBlogForm(instance=edit_blog)
  return render(request,'dashboard/edit_blog_form.html',{'editform_key': edit_blog_form})

  