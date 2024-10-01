from django.urls import path 
from .views import IndexPageView 
from .views import LibroPageView 
urlpatterns = [ 
path("", IndexPageView.as_view(), name="index"),
path("book/", LibroPageView.as_view(), name="libro"), ]