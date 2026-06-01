from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Review, Comment


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
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
    approve_comments.short_description = "Approve selected comments"

# Register your models here.


admin.site.register(Comment, CommentAdmin)
