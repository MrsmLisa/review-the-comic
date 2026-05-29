from django.shortcuts import render, get_object_or_404
from .models import Review
from django.views.generic import ListView, DetailView
from .forms import CommentForm

# Create your views here.


class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/index.html'
    context_object_name = 'reviews'
    queryset = Review.objects.filter(status=1).order_by('-created_at')
    paginate_by = 6

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'reviews/review_detail.html'
    context_object_name = 'review'
    slug_url_kwarg = 'slug'

def review_detail(request, slug):
    review = get_object_or_404(Review, slug=slug, status=1)
    comment_form = CommentForm()

    return render(request, 'reviews/review_detail.html', {
        'review': review,
        'comment_form': comment_form
    })
    
    