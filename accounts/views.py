from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import auth
from .models import Student
from  django.shortcuts import get_object_or_404

@login_required(login_url="./login")
#redirect to login page if not registered
def dashboard(request):
    context = {
    }
    return render(request, 'accounts/dashboard.html', context)


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("dashboard")
        else:
            return redirect("login")
    else:
        return render(request, "accounts/login.html")

def logout(request):
    if request.method == "POST":
        auth.logout(request)
    return redirect("login")