from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



# Create your views here.
def show_cars(request):
    return render(request,'cars/index.html') 

def add_cars(request):
    return render(request,'cars/add.html')

def update_cars(request):
    return render(request,'cars/update.html')
