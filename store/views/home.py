from itertools import product
from django.shortcuts import redirect, render
from django.views import View
from store.models.product import Products
from store.models.category import Category

class Home(View):
    def get(self,request):
        category = Category.objects.all()
        product = None
        categoryID = request.GET.get('category')
        if categoryID:
            product = Products.get_data_by_id(categoryID)
        else:
            product = Products.objects.all()
        data = {
            'category':category,
            'product':product
        }
        return render(request,'home.html',data)
    def post(self,request):
        return redirect('/')