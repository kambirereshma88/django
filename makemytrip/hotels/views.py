from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_hotels(request):
    msg="<h1>welcome to mmt hotels</h1>"
    return HttpResponse(msg)

def update_hotels(request):
    msg="<h1>update hotels</h1>"
    return HttpResponse(msg)

def delete_hotels(request):
    msg="<h1>delete hotels</h1>"
    return HttpResponse(msg)



