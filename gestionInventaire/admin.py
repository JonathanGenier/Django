from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class ViewAdmin(admin.ModelAdmin):
    pass