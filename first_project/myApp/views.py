from django.http import *
from django.shortcuts import render
import datetime

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


def get_category(request,category):
    try:
        products = data[category]
        return render(request,"products.html",{
            "category":category,
            "products":products,
            "now":datetime.datetime.now
        })
    except:
        return HttpResponseNotFound("Page is not found.")
