from django.urls import reverse_lazy
from django.urls import path
from . import views

urlspatterns = [
    path('', views.index, name='index'),
    path(' /<int: advert_id>/', views.detail, name='detail')

]