from django.contrib import admin
from second_app.models import *

# Register your models here.  
class PostAdmin(admin.ModelAdmin):
  list_display= ('title', 'user','status','created_on')
  list_filter= ("status",)
  search_fields =['title', 'content']
  prepopulated_fields= {'slug': ('title',)}



class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)





admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(UserProfile) 
admin.site.register(Contacts)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Work)
admin.site.register(Skill)


admin.site.site_header='Ayomiposhh'

