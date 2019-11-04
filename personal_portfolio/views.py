from django.shortcuts import render
from django.urls import path

def about(request):
    return render(request,"about.html")
