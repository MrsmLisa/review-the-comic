from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class Review(models.Model):
    title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=100)  # author of the book
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    status = models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)
    excerpt = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
