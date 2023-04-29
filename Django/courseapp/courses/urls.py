from django.contrib import admin
from django.urls import path
from . import  views
from django.shortcuts import render

from django.http import HttpResponse

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home),
    path("anasayfa", views.home),
    path("kurslar", views.kurslar)
]
