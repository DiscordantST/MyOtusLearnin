from django.urls import path

from . import views
from .views import BlogListView, BlogDetailView


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post_list/', BlogListView.as_view(), name='post_list'),


]
