from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Blog


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'content', 'image', 'is_published']
    success_url = reverse_lazy('blog:blog_views')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'image', 'is_published']
    success_url = reverse_lazy('blog:blog_views')


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_views')
