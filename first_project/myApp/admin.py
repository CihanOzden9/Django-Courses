from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","price","isActive","slug")
    list_editable = ("isActive",)
    list_display_links = ("name","price",)
    search_fields = ("name",)

# Register your models here.
admin.site.register(Product,ProductAdmin)