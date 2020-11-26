from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from.models import User
# Create your views here.

def index(request):
    return render(request,"user/login.html")

def login(request):
    if(request.method=="POST"):
        message="No such user exists."
        username=request.POST.get("username")
        password=request.POST.get("password")
        if(User.objects.get(username=username, password=password)):
            return HttpResponse("Logged in")
        elif(User.objects.get(username=username) or User.objects.get(password=password)):
            message="Invalid Username/ password"
        return render(request, "user/login.html", {
            "message": "Invalid Username/ Password."
        })
    return render(request, "user/login.html")

def logout(request):
    return HttpResponse("Logout")

def signup(request):
    if(request.method=="POST"):
        # check if username is taken , also check if the name is unique
        user=User()
        user.fname=request.POST.get("fname")
        user.lname=request.POST.get("lname")
        user.username = request.POST.get("username")

        # add- checking if the username is already used or not

        if(request.POST.get("password1")==request.POST.get("password2")):
            user.password = request.POST.get("password1")
        else:
            return render(request,"user/signup.html",{
                "password_message": "Passwords do not match, try again ! "
            })

        user.save()

    return render(request,"user/signup.html")
