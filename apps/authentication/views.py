from django.shortcuts import render, redirect
from .forms import RegistrationForm

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
    return render(request, "signin.html")