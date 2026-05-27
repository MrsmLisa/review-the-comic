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

# Register your models here.

