from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify



# Create your models here.


class Review(models.Model):
    title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=200)  # author of the book
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    status = models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=1)
    excerpt = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    likes = models.ManyToManyField(User, related_name='liked_reviews')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
    def review_url(self):
        return reverse('review_detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def total_likes(self):
        return self.likes.count()    

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'Comment by {self.author} on {self.review}'
    