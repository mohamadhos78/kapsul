from django.shortcuts import render

def dashboard(request):
    context = {
    }
    return render(request, 'accounts/dashboard.html', context)


def login(request):
    context = {
    }
    return render(request, "accounts/login.html",context)