
from django.contrib import admin
from django.urls import path
from views import IndexClass,NewClass,ShowClass 

urlpatterns = [
  path('admin/', admin.site.urls),
  path('index',IndexClass.as_view()),
  path('new',NewClass.as_view()), 
  path('show',ShowClass.as_view()), 
]
