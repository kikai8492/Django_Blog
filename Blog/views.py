from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Blog
from .forms import BlogForm
from django.shortcuts import render

class Index(TemplateView):
  template_name = "index.html"
  blogs = Blog.objects.all()

def new(request):
  template_name = "new.html"
  form = BlogForm
  context = {'form': form}
  return render(request, 'index.html', context)

class Show(TemplateView): 
  template_name = "show.html"