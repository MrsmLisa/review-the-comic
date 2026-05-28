from xml.etree.ElementTree import Comment

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Review

@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    list_display = ('title', 'book_author', 'created_at', 'status')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'book_author')
    list_filter = ('status', 'created_at')
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'review', 'created_at')
    search_fields = ('author', 'content')
    list_filter = ('created_at',)    

# Register your models here.

admin.site.register(Comment, CommentAdmin)