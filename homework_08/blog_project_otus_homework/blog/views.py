from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post
from .form import CreatePost, UpdatePost


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


class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    form_class = CreatePost


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    form_class = UpdatePost


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')
