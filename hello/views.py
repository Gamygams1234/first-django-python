from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    # redering a template
    return render(request, "hello/index.html")


def gamy(request):
    return HttpResponse('Hello, Gamy')


def greet(request, name):
    # optional third argument which is info provided to the template
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
