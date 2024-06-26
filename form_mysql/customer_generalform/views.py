from django.shortcuts import render
from customer_generalform import forms
from django.http import HttpResponse

# Create your views here.
def add(request):
    if(request.method=="GET"):
         customer_form = forms.customerform()
         data ={}
         data['form']=customer_form
         return render(request,'customer/add.html',context=data)
    else:
         customer_data=forms.customerform(request.POST)
         if(customer_data.is_valid()):
              customer_data.save(commit=True)
              return HttpResponse("Customer added, Please check your table")
