
from django.contrib import admin
from django.urls import path
from .views import Index,new,Show


urlpatterns = [
  path('admin/', admin.site.urls),
  path('',Index.as_view(), name='index'),
  path('new',new, name='new'), 
  path('show',Show.as_view(), name='show'), 
]
