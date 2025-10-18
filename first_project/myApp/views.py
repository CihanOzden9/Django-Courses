from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Merhaba")
def details(request):
    return HttpResponse("Details")
def list(request):
    return HttpResponse("List")