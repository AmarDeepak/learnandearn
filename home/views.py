from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import loader

def home(request):
    context = {
        'sometext': "Hello World",
    }
    return render(request, 'home/home.html', context)
