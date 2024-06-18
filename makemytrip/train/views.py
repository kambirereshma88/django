from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_train(request):
    msg="<h1>welcome to mmt train</h1>"
    return HttpResponse(msg)

def update_train(request):
    msg="<h1>update train</h1>"
    return HttpResponse(msg)

def delete_train(request):
    msg="<h1>delete train</h1>"
    return HttpResponse(msg)



