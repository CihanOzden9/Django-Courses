from django.http import *
from django.shortcuts import render
import datetime
from .models import Product

veriler = {
    "telefon":["samsung","apple","xiaomi"],
    "bilgisayar":["laptop","macbook","setup"],
    "elektronik":["çamaşır","bulaşık"],
    "araba":[],
    "armut":["hayır","evet"]
}

# Create your views here.
def index(request):
    categories = list(veriler.keys())
    return render(request, "index.html",{
        "categories":categories,
        "page":"index",
    })


def create(request):
    if request.method == 'POST':
        product_name = request.POST['name']
        price = request.POST['price']
        description = request.POST['description']
        image_url = request.POST['image_url']
        category = request.POST['category']

        product = Product(name=product_name, price=price,description=description,imageUrl=image_url,category=category)
        product.save()
        return HttpResponseRedirect("/")
    return render(request,"create.html")



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
