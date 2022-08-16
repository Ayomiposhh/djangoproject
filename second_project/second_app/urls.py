from django.urls import path, include 
from second_app import views
from django.contrib.auth import views as auth_views

# from second_project import second_app


app_name = 'second_app'


urlpatterns = [
   
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('edit-profile/', views.edit, name='edit'),
    path('edit_pass/',views.pass_change, name='edit_pass'),
    path('blog/',views.BlogList.as_view(),name='blog'),
    path('viewblog/',views.viewblog, name='view_blog'),
    path('viewdetail/<int:post_id>',views.viewdetail, name='view_detail'),
    path('addblog/',views.Addblog.as_view(),name='add_blog'),
    path('edit_blog/<int:post_id>',views.updateblog, name='edit_blog_form'),
    path('delete/<int:post_id>', views.delete_post,name='delete'),
    # path('update_blog/<int:pk>', views.UpdateBlog.as_view(),name='update_blog'),
    path('view_profile/', views.viewprofile,name='view_profile'),
    path('<slug:slug>/', views.post_detail, name='blog_detail'),
    # path('<slug:slug>/', views.BlogDetail.as_view(),name='blog_detail'),
    
   
    
    
    

]
