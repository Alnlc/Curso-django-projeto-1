from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def home(request):
    return render (request,"recipes/pages/home.html", context={
        'name': 'Zéze de camargo'
    })