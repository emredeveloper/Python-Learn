from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("<strong> Welcome to Course App </strong>")


def kurslar(request):
    return HttpResponse("<strong> Kurslar </strong>")
