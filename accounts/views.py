from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.get(username=request.POST["username"])
                return render(request, 'accounts/signup.html',
                          {'error': 'Username has been already taken!'})
        
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST["username"], password=request.POST["password1"])
                auth.login(request, user)
                return redirect('home')

        else:
            return render(request, 'accounts/signup.html',
                          {'error': 'Password Does Not Allowed!'})
                
    
    else:
        return render(request, 'accounts/signup.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html',
                          {'error': 'Account Invalid!'})
 
    else:        
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)

        return redirect('accounts:login')
