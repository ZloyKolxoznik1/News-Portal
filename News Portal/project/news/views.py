from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import *


class NewsList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'post.html'
    context_object_name = 'post'


class NewsDetail(DetailView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'