from django.contrib import admin
from store.models.register import Register

from store.models.category import Category
from store.models.product import Products



class Cat(admin.ModelAdmin):
    list_display=['name']

admin.site.register(Category,Cat)

class Reg(admin.ModelAdmin):
    list_display = ['name','email','password','phone']

admin.site.register(Register,Reg)

class Pro(admin.ModelAdmin):
    list_display=['name','price','category','desc','images']

admin.site.register(Products,Pro)
# Register your models here.
