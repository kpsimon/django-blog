from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'author': 'Keoni',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 29, 2021'
    },
    {
        'author': 'John',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 30, 2021'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
