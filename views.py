from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

@login_required(login_url="login/")
def home(request):
    return render(request,"home.html")
def signup(request):
    if request.method != "POST":
        return render(request,"register.html")
    uname = request.POST.get("rname",'')
    fname = request.POST.get("fname",'')
    lname = request.POST.get("lname",'')
    remail = request.POST.get("remail",'')
    passwd = request.POST.get("rpasswd",'')
    user = None
    try:
        user = User.objects.get(username=uname)
    except ObjectDoesNotExist:
        user = None
    if user:
        return render(request,"register.html")
    user = User.objects.create_user(username=uname,first_name=fname,last_name=lname,
            email=remail,password=passwd)
    user.is_active = True
    user.save()
    login(request,user)
    return render(request,"home.html")

