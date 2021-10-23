# from django.http import HttpResponse
from django.shortcuts import render
from .models import Talk, Games

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


def games(request):
    games_list = Games.objects.all()
    context = {"games": games_list}
    return render(request, "games.html", context)


# def customers(request):
#     customers_list = Customers.objects.all()
#     context = {"customers": customers_list}
#     return render(request, "games.html", context)
