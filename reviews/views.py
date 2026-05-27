from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'reviews/index.html')

def review_detail(request, slug):
    return render(request, 'reviews/review_detail.html', {'slug': slug})

