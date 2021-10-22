# from django.http import HttpResponse
from django.shortcuts import render
from .models import Talk

# Create your views here.


# def index(request):
#     return HttpResponse('<h1 style="font-family: sans-serif">Isabel Project</h1>')


# def index(request):
#    return render(request, 'index.html')


def index(request):
    talk = Talk.objects.all()
    context = {"talks": talk}
    return render(
        request,
        "index.html",
        context,
    )
