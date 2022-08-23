from django.shortcuts import render
from .models import KSU_SHOP


def home(request):
    posts = KSU_SHOP.objects.all()
    context = {'posts': posts}
    return render(request, 'home.html', context)