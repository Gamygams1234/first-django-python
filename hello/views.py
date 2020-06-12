from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    # redering a template
    return render(request, "hello/index.html")


def gamy(request):
    return HttpResponse('Hello, Gamy')


def greet(request, name):
    return HttpResponse(f'Hello, {name.capitalize()}')
