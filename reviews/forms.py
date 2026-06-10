from django import forms
from .models import Comment, Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = [
            "title",
            "featured_image",
            "book_author",
            "content",
            "excerpt",
        ]

    def featured_image(self):
        image = self.cleaned_data.get("featured_image")
        if not image:
            raise forms.ValidationError(
                "Please upload a cover image for your review."
            )
        return image


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["content"]
