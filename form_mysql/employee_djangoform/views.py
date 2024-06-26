from django.shortcuts import render
from django.http import HttpResponse
from employee_djangoform.forms import EmployeeForm
from employee_djangoform.models import Employee 

# Create your views here.
def add(request):
     employee_form = EmployeeForm() #to show form
     data={}
     data['form'] = employee_form
     if (request.method =="POST"):
         employeeFormData = EmployeeForm(request.POST)  #to collect data from form
         employee = Employee()   #object of model class
         if (employeeFormData.is_valid()):
             employee.name = employeeFormData.cleaned_data['name']
             employee.phone = employeeFormData.cleaned_data['phone']
             employee.salary = employeeFormData.cleaned_data['salary']
             print(employee.name,employee.phone,employee.salary)
             employee.save()
             return HttpResponse("Employee added,please check your table")
     return render(request,'employee/add.html',context=data)
