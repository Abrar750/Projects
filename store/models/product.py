from unicodedata import category
from django.db import models

from store.models.category import Category

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    desc = models.CharField(max_length=200,default="")
    images = models.ImageField(upload_to = "static/img/")
    
    @staticmethod
    def get_data_by_id(category_id):
        if category_id:
            return Products.objects.filter(category = category_id)
        else:
            return Products.objects.all()