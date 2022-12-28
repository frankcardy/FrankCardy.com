from django.shortcuts import render
from django.utils import timezone
from .models import Post

from django.views.generic import ListView, DetailView

# Create your views here.
#def index(request):
   # return HttpResponse("Hello, this is the beginning of my CTF writeup blog")
'''
def post_list(request):
   posts = Post.objects.order_by('published_date')
   return render(request, 'blog/post_list.html', {'posts': posts})
'''

'''
def post_list(request):
   posts = Post.objects.all
   return render(request, 'blog/post_list.html', {'posts': posts})
'''

class PostView(ListView):
   model = Post
   #template_name = 'post_list.html'
   template_name = 'blog/post_list_test.html'

class PostDetailView(DetailView):
   model = Post
   template_name = 'blog/post_details.html'

class AboutView(ListView):
   model = Post
   template_name = 'blog/about.html'

