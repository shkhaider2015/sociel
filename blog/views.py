from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# posts = [
#     {
#         'author' : 'Shakeel Haider',
#         'title' : 'blog post 1',
#         'content' : 'this is post 1 content',
#         'date_posted' : 'Novenmber 3, 2019'
#     },
#     {
#         'author' : 'Dawood Haider',
#         'title' : 'blog post 2',
#         'content' : 'this is post 2 content',
#         'date_posted' : 'Novenmber 4, 2019'
#     }
# ]

# Create your views here.
def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    