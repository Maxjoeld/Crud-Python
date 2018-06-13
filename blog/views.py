from django.shortcuts import render
from blog.models import Post,Comment
from blog.forms import PostForm, CommentForm
# this wait for post to be deleted for success page 
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView, 
DetailView, CreateView, UpdateView, DeleteView)


class AboutView(TemplateView):
  template_name = 'about.html'

class PostListView(ListView):
  model = Post

  def get_query_set(self): # __less than or equal to--look this up 
    #grab the published dates that are less than or equal to the current time then order by publish date 
    # the dash lets you decided between ascending or descending order
    # in our case the dash resembles descending 
    # look up keyword arguments in python to read more about it 
    return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
  model = Post

class CreatePostView(LoginRequiredMixin,CreateView):
  login_url = '/login/'
  redirect_field_name = 'blog/post_detail.html'
  form_class = PostForm
  model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
  login_url = '/login/'
  redirect_field_name = 'blog/post_detail.html'
  form_class = PostForm
  model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
  model = Post 
  success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin, ListView):
  login_url = '/login/'
  redirect_field_name = 'blog/post_list.html'
  model = Post

  def get_queryset(self):
    return Post.objects.filter(published_date_isnull=true).order_by('created_date')