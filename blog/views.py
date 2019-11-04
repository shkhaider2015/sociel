from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'Shakeel Haider',
        'title' : 'blog post 1',
        'content' : 'this is post 1 content',
        'date_posted' : 'Novenmber 3, 2019'
    },
    {
        'author' : 'Dawood Haider',
        'title' : 'blog post 2',
        'content' : 'this is post 2 content',
        'date_posted' : 'Novenmber 4, 2019'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')