from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_customer(request):
    #msg = "<h1>welcome customer</h1>"
    #return HttpResponse(msg)
    customer_data={'name':'reshma','age':28}
    return render(request,'customer/index.html',context=customer_data)

def update_customer(request):
    msg = "<h1> update customer</h1>"
    return HttpResponse(msg)

def delete_customer(request):
    msg ="<h1> delete customer </h1>"
    return HttpResponse(msg)
