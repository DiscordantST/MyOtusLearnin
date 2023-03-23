from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


def home(request):
    return render(template_name='blog/base.html', request=request)


def about(request):
    return render(template_name='blog/about.html', request=request)


class BlogListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
