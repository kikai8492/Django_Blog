from django.http import HttpResponse
from django.views.generic import TemplateView

class IndexClass(TemplateView):
  template_name = "index.html"

class NewClass(TemplateView):
  template_name = "new.html"

class ShowClass(TemplateView):
  template_name = "show.html"