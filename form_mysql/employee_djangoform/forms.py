from django import forms

# Create your models here.
class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=50)
    salary = forms.FloatField()
