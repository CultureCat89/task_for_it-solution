# from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def my_first_view(request):
    return HttpResponse("Hello! It's my first view!!!")