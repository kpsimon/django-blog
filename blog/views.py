from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post

    # looking for <app>/<model>_<viewtype>.html or blog/post_list.html
    template_name = 'blog/home.html'
    context_object_name = 'posts'

    # sort by newest post first
    ordering = ['-date_posted']

    # pagination here
    paginate_by = 5

class UserPostListView(ListView):
    model = Post

    # looking for <app>/<model>_<viewtype>.html or blog/post_list.html
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'

    # pagination here
    paginate_by = 5

    def get_queryset(self):
        #get user from url and order from new to old
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
    model = Post
    # looking for <app>/<model>_<viewtype>.html or blog/post_detail.html

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post

    # fields to add in the form
    fields = ['title', 'content']

    def form_valid(self, form):
        # override form valid to add author
        form.instance.author = self.request.user
        return super().form_valid(form)

# required login and author = current user
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post

    # fields to add in the form
    fields = ['title', 'content']

    def form_valid(self, form):
        # override form valid to add author
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        # check if current logged in user is author
        if self.request.user == post.author:
            return True
        return False

# required login and author = current user
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    # looking for <app>/<model>_<viewtype>.html or blog/post_detail.html

    def test_func(self):
        post = self.get_object()
        # check if current logged in user is author
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
