from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show(request):
    return render(request,'product/show.html')

def add(request):
    return render(request,'product/add.html')

def update(request):
    return render(request,'product/update.html')
    
