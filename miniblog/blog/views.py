from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
import time
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from blog.form import user_form

# Create your views here.

# home: 
def home(request):
    return render(request, "blog/home.html")

# about:
def about(request):
    return render(request, "blog/about.html")

# Dashboard
def dashboard(request):
    return render(request, "blog/dashboard.html")

# Login:
def user_login(request):
    if request.method == 'POST':
        fm =AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                messages.MessageFailure(request, "username and password not matched")
    else:
        fm = AuthenticationForm()
        print("form is visble")
    return render(request, 'blog/login.html', {'form': fm})

# Signup:
def user_signup(request):
    if request.method == 'POST':
        fm = user_form(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'your account is created!!')
            time.sleep(2)
            return HttpResponseRedirect('/login/')

    else:
        fm = user_form()
    return render(request, "blog/signup.html", {'form': fm})

# contact:
def contact(request):
    return render(request, "blog/contact.html")

# logout:
def logout(request):
    return render(request, "blog/logout.html")


