from django.urls import path
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import views

app_name = 'main2'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path(' /<int:advert_id>/', views.DetailView.as_view(), name='detail'),
]