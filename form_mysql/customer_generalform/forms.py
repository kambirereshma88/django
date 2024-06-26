from django import forms
from customer_generalform import models

class customerform(forms.ModelForm):
    class Meta:
        model=models.customer 
        fields=('name','phone','city')
        