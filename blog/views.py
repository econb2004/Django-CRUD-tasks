from dataclasses import field
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
# Create your views here.

from .models import *
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "post_list.html"


class PostCreateView(CreateView):
    model = Post
    fields = "_all_"
    success_url = reverse_lazy("blog:all")
    template_name = "post_form.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class PostUpdateView(UpdateView):
    model = Post
    fields = "_all_"
    success_url = reverse_lazy("blog:all")
    template_name = "post_list.html"


class PostDeleteView(UpdateView):
    model = Post
    fields = "_all_"
    success_url = reverse_lazy("blog:all")
    template_name = "post_confirm_delete.html"
