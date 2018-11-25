from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Advert

class IndexView(generic.ListView):
    template_name = 'main2/index.html'
    context_object_name = 'latest_question_list'

    def get_adverts(self):
        return Advert.objects.all()

class DetailView(generic.DetailView):
    model = Advert
    template_name = 'main2/detail.html'
