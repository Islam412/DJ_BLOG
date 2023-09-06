from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post , Comment



class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ['title','draft','author']
    list_filter = ['draft','author']
    search_fields = ['title','content']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','post','create_at']
    list_filter = ['user']

# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.site_header = 'BLOG'
admin.site.site_title = 'BLOG'