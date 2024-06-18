from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def show_product(request):
    #msg ="<h1> welcome product </h1>"
    #return HttpResponse(msg)
    return render(request,'product/index.html')

def update_product(request):
    msg ="<h1> update product </h1>"
    return HttpResponse(msg)

def delete_product(request):
    msg ="<h1> delete product </h1>"
    return HttpResponse(msg)
