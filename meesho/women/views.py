from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_women(request):
    return render(request,'women/index.html')

def update_women(request):
    return render(request,'women/update.html')

def add_women(request):
    return render(request,'women/add.html')


