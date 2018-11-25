from django.shortcuts import render, get_object_or_404
from .models import Advert



def index(request):
    return render(request, 'main/detail.html', {})

def detail(request, advert_id):
    advert = get_object_or_404(Advert, pk=advert_id)
    return render(request, 'main/detail.html', {'advert': advert})



