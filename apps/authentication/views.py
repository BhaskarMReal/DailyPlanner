from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, LoginForm



def signup(request): 
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
   
    else: 
        form = RegistrationForm()
    return render(request, "signup.html", {'form': form})

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            print(email, password)
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("daily")
            else:
                return redirect("signin")
    else:
        form = LoginForm()
    return render(request, "signin.html", {'form':form})