from django.shortcuts import render, redirect
from .models import Advertisements
from .forms import AdvertisementForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required


@login_required(login_url=reverse_lazy('login'))


def index(request):
    advertisiments = Advertisements.objects.all()
    context = {'advertisiments': advertisiments}
    return render(request, 'app_advertisiments/index.html', context)

def top_sellers(request):
    return render(request, 'app_advertisiments/top-sellers.html')


def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisements(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm
    context = {'form': form}
    return render(request, 'app_advertisiments/advertisement-post.html', context)