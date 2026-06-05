from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from requests import post, request
from .models import Review
from django.views.generic import ListView, DetailView
from .forms import CommentForm
from .forms import ReviewForm
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse


#review main page


class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/index.html'
    context_object_name = 'reviews'
    queryset = Review.objects.filter(status=1).order_by('-created_at')
    paginate_by = 6

# review detail page


class ReviewDetailView(DetailView):
    model = Review
    template_name = 'reviews/review_detail.html'
    context_object_name = 'review'
    slug_url_kwarg = 'slug'


def review_detail(request, slug):
    review = get_object_or_404(Review, slug=slug, status=1)
    comments = review.comments.all().order_by('-created_at')
    comment_form = CommentForm()
    post_is_liked = False
    post_is_liked = review.likes.filter(id=request.user.id).exists()

    return render(request, 'reviews/review_detail.html', {
        'review': review,
        'comments': comments,
        'comment_form': comment_form,
        'post_is_liked': post_is_liked,
        'Total_likes': review.total_likes()
    })

# comment form for review detail page


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
            messages.info(request, 'Your comment has been submitted.')
            return redirect('review_detail', slug=slug)
    else:
        comment_form = CommentForm()

    return render(request, 'reviews/review_detail.html', {
        'review': review,
        'comment_form': comment_form
    })

# review creation form


@login_required
def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
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


def review_like(request, slug):
    review = get_object_or_404(Review, slug=slug)
    if review.likes.filter(id=request.user.id).exists():
        review.likes.remove(request.user)
    else:
        review.likes.add(request.user)
    return redirect('review_detail', slug=slug)


@login_required
def editPost(request, slug):
    review = get_object_or_404(Review, slug=slug)
    if review.author != request.user:
        messages.error(request, 'You are not authorized to edit this review.')
        return redirect('review_detail', slug=slug)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review updated successfully.')
            return redirect('review_detail', slug=slug)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviews/review_form.html', {'form': form, 'editing': True})


@login_required
def deletePost(request, slug):
    review = get_object_or_404(Review, slug=slug)
    if review.author != request.user:
        messages.error(request, 'You are not authorized to delete this review.')
        return redirect('review_detail', slug=slug)
    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Review deleted successfully.')
        return redirect('index')
    return render(request, 'reviews/confirm_delete.html', {'review': review})

# review like view


class ReviewLikeView(DetailView):
    model = Review
    template_name = 'reviews/review_detail.html'
    context_object_name = 'review'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        like_connected = get_object_or_404(Review, slug=self.kwargs['slug'])
        if like_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['post_is_liked'] = liked
        data['total_likes'] = like_connected.total_likes()
        return data

def handler_404_view(request, exception):
    return render(request, '404.html', status=404)

def handler_500_view(request):
    return render(request, '500.html', status=500)