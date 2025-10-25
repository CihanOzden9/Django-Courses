from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    #path('<category>',views.get_category,name="products"), #<category> bize dinamik web adresini döndürecek
    path('list',views.list)
]