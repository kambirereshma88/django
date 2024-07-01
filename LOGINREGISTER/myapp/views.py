from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    data={}
    if (request.method=="POST"):
        uname=request.POST['username']
        upass=request.POST['password']
        ucpass=request.POST['cpassword']
        ucpass=request.POST['cpassword']
        #print(username,password,cpassword)
        
        if (uname=="" or upass=="" or ucpass==""):
            #print("fields cant be empty")
            data["error_msg"]="feilds cant be empty"
            
        elif(upass!=ucpass):
            print("password does not matched")
            
            #from django.contib.auth.models import User
        elif(User.objects.filter(username=uname).exists()):
            #print(uname + "is already exist")
            data['error_msg']=uname + "is already exist"
        
        else:
            user=User.objects.create(username=uname)
            user.set_password(upass)
            user.save()    
        return HttpResponse("Done")
    return render (request,'myapp/register.html')
    
            
