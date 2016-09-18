from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import Bank
import requests as prequests
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
import json as pjson


# Create your views here.
apiKey = '87b023161ebf538b86a016bc0ac005fc'

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

@login_required(login_url="login/")
def home(request):
    return render(request,"home.html")
def signup(request):
    emsg = ""
    if request.method != "POST":
        return render(request,"register.html")
    uname = request.POST.get("rname",'')
    fname = request.POST.get("fname",'')
    lname = request.POST.get("lname",'')
    remail = request.POST.get("remail",'')
    streetn = request.POST.get('stname','')
    streeti = request.POST.get('stnumber','')
    city = request.POST.get('rcity','')
    state = request.POST.get('rstate','')
    zipcode = request.POST.get('rzip','')
    passwd = request.POST.get("rpasswd",'')
    cpasswd = request.POST.get("cpasswd",'')
    if passwd != cpasswd:
        emsg = "Password does not match!"
        return render(request,"register.html",{'emsg':emsg})
    user = None
    try:
        user = User.objects.get(username=uname)
    except ObjectDoesNotExist:
        user = None
    if user:
        emsg = "Username already exists!"
        return render(request,"register.html",{'emsg':emsg})
    user = User.objects.create_user(username=uname,first_name=fname,last_name=lname,
            email=remail,password=passwd)
    user.is_active = True

    payload = {
      "first_name": fname,
      "last_name": lname,
      "address": {
	"street_number": streeti,
	"street_name": streetn,
	"city": city,
	"state": state,
	"zip": zipcode
      }
    }
    bankurl = 'http://api.reimaginebanking.com/customers?key={}'.format(apiKey)
    response = prequests.post(bankurl, data=pjson.dumps(payload),
            headers={'content-type':'application/json'},)
    if response.status_code == 201:
        user.save()
        login(request,user)
        return render(request,"home.html")
    emsg = "System busy, try again later!"
    return render(request,"register.html",{'emsg':emsg})
