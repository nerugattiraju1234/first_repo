from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from firstapp.forms import signupform
from django.http import HttpResponseRedirect

# Create your views here.
def home_view(request):
    return render(request,"firstapp/home.html")
@login_required
def java_view(request):
    return render(request,"firstapp/java.html")
@login_required
def python_view(request):
    return render(request,"firstapp/python.html")
@login_required
def linux_view(request):
    return render(request,"firstapp/linux.html")
def logout_view(request):
    return render(request,"firstapp/logout.html")
def signup_view(request):
    form=signupform()
    if request.method=="POST":
        form=signupform(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect("/accounts/login")
    return render(request,"firstapp/signup.html",{"form":form})
