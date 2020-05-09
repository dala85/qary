from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from . import models

# Create your views here.


class PostListView(ListView):
    context_object_name = 'posts'
    model = models.Post


class PostDetailView(DetailView):
    context_object_name = 'post_detail'
    model = models.Post
    template_name = 'qary_post/qary_post_detail.html'
