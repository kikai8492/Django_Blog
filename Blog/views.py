from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Blog

class IndexClass(TemplateView):
  template_name = "index.html"
  blogs = Blog.objects.all()

class NewClass(TemplateView):
  template_name = "new.html"

class ShowClass(TemplateView):
  template_name = "show.html"