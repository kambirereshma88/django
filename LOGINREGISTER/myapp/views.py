from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    data={}
    if(request.user.is_authenticated):
        user_id=request.user.id
        user=User.objects.get(id=user_id)
        data['username']=user.username
    return render(request,'myapp/home.html',context=data )




def register(request):
    data={}
    if (request.method=="POST"):
        uname=request.POST['username']
        upass=request.POST['password']
        ucpass=request.POST['cpassword']
        #print(username,password,cpassword)
        
        if(uname=="" or upass=="" or ucpass==""):
         # print("fields cant be empty")
         data['error_msg']="fields cant be empty"
         return render(request,'myapp/register.html',context=data)
        elif(upass!=ucpass):
         # print("password doen not matched")
         data['error_msg']="password does not matched"
         return render(request,'myapp/register.html',context=data)
         #from django.contrib.auth.models import User
        elif(User.objects.filter(username=uname).exists()):
         # print(uname + " is already exist")
         data['error_msg']=uname + " is already exist"
         return render(request,'myapp/register.html',context=data)
        else:
         user=User.objects.create(username=uname)
         user.set_password(upass)
         user.save()
        # return HttpResponse("DONE")
        return redirect ('/myapp/login')
    return render(request,'myapp/register.html',context=data)


def user_login(request):
    data={}
    if (request.method=="POST"):
        uname=request.POST['username']
        upass=request.POST['password']
    

        if(uname=="" or upass==""):
         # print("fields cant be empty")
         data['error_msg']="fields cant be empty"
         return render(request,'myapp/login.html',context=data)       
     
        elif( not User.objects.filter(username=uname).exists()):
         # print(uname + " is already exist")
         data['error_msg']=uname + "  does not exist"
         return render(request,'myapp/login.html',context=data)
        
        else:
            user = authenticate(username=uname, password=upass)
            if user is None:
                data['error_msg']="wrong password"
                return render (request,'myapp/login.html',context=data)
            else:
                login(request,user)
                return redirect('/myapp/home/')
    return render(request,'myapp/login.html',context=data)

def user_logout(request):
    logout(request)
    return redirect('/myapp/home/')
    

         
        
            
