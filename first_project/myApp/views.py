from django.http import *
from django.shortcuts import render
import datetime
from .models import Product

data = {
    "telefon":["samsung","apple","xiaomi"],
    "bilgisayar":["laptop","macbook","setup"],
    "elektronik":["çamaşır","bulaşık"],
    "araba":[],
    "armut":["hayır","evet"]
}

# Create your views here.
def index(request):
    categories = list(data.keys())
    return render(request, "index.html",{
        "categories":categories,
        "page":"index",
    })


def list(request):
    q = request.GET['q']
    render(request, "list.html",q)

def get_category(request,category):
    try:
        products = Product.objects.all()
        context = {
            "category":category,
            "products":products,
            "now":datetime.datetime.now
        }
        
        return render(request,"products.html",context)
    except:
        return HttpResponseNotFound("Page is not found.")
