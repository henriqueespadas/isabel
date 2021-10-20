# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# def index(request):
#     return HttpResponse('<h1 style="font-family: sans-serif">Isabel Project</h1>')
#


def index(request):
    return render(request, "index.html")
