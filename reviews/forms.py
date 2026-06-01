from django import forms
from .models import Comment, Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['title', 'featured_image', 'book_author', 'content', 'excerpt']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']
