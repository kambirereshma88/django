from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_bus(request):
    msg="<h1>welcome to mmt bus</h1>"
    return HttpResponse(msg)

def update_bus(request):
    msg="<h1>update bus</h1>"
    return HttpResponse(msg)

def delete_bus(request):
    msg="<h1>delete bus</h1>"
    return HttpResponse(msg)




