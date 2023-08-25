from django.shortcuts import render
from .models import Advertisements

def index(request):
    advertisiments = Advertisements.objects.all()
    context = {'advertisiments': advertisiments}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')