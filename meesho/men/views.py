from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_men(request):
    return render(request,'men/index.html')
def update_men(request):
    return render(request,'men/update.html')
def add_men(request):
    return render(request,'men/add.html')


    
