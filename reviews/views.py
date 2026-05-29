from django.shortcuts import redirect, render, get_object_or_404
from .models import Review
from django.views.generic import ListView, DetailView
from .forms import CommentForm
from .forms import ReviewForm
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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

@login_required
def comment_review(request, slug):
    review = get_object_or_404(Review, slug=slug)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment added successfully.')
            return redirect('review_detail', slug=slug)
    else:
        comment_form = CommentForm()

    return render(request, 'reviews/review_detail.html', {
        'comment_form': comment_form
    })

@login_required
def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.slug = slugify(review.title)
            review.save()
            messages.success(request, 'Review created successfully.')
            return redirect('index')
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_form.html', {'form': form})    