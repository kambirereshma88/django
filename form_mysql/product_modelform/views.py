from django.shortcuts import render
from django.http import HttpResponse
from  product_modelform.models import Product

# Create your views here.
def add(request):
    if (request.method=="POST"):
        pname=request.POST['name']
        pprice=request.POST['price']
        pcategory=request.POST['category']
        print(pname, pprice, pcategory)
        #product.objects.create(column_name=value)
        product= Product.objects.create(name=pname, price=pprice, category=pcategory)
        product.save()
        return HttpResponse("DONE")   
    return render(request,'product/add.html')
