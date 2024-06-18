from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def show_bus(request):
    return render(request,'bus/index.html') 

def add_bus(request):
    return render(request,'bus/add.html')

def update_bus(request):
    return render(request,'bus/update.html')