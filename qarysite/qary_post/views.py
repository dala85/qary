from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from . import models
from django.urls import reverse_lazy


# Create your views here.


class PostListView(ListView):
    context_object_name = 'posts'
    model = models.Post


class PostDetailView(DetailView):
    context_object_name = 'post_detail'
    model = models.Post
    template_name = 'qary_post/post_detail.html'


class PostCreateView(CreateView):

    fields = ('author', 'title', 'text')
    model = models.Post


class PostUpdateView(UpdateView):

    fields = ('title', 'text')
    model = models.Post


class PostDeleteView(DeleteView):

    model = models.Post
    success_url = reverse_lazy('qary_post:list')
