from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
import time
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from blog.form import user_form, blog_form
from .models import Post

# Create your views here.

# home: 
def home(request):
    posts = Post.objects.all()
    return render(request, "blog/home.html", {'posts': posts})

# about:
def about(request):
    return render(request, "blog/about.html")

# Dashboard
def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        return render(request, "blog/dashboard.html", {'stub':posts})
    else:
        return HttpResponseRedirect('/login/')

# Login:
def user_login(request):
    if not request.user.is_authenticated:
      if request.method == 'POST':
          fm =AuthenticationForm(request=request, data=request.POST)
          if fm.is_valid():
              uname = fm.cleaned_data['username']
              upass = fm.cleaned_data['password']
              user = authenticate(username=uname, password=upass)
              if user is not None:
                  login(request, user)
                  messages.success(request, 'Logged In!!')
                  return HttpResponseRedirect('/dashboard/')
              
      else:
          fm = AuthenticationForm()
      return render(request, 'blog/login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/dashboard/')

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
def user_logout(request):
        logout(request)
        return HttpResponseRedirect('/login/')

# delete:
def delete_data(request, id):
    if request.user.is_authenticated:
      if request.method == "POST":
         pi = Post.objects.get(pk=id)
         pi.delete()
         return HttpResponseRedirect('/dashboard/')
    else:
      return HttpResponseRedirect('/login/')

# update:   
def update_data(request, id):
   if request.user.is_authenticated:
      if request.method == 'POST':
        pi = Post.objects.get(pk=id)
        fm = blog_form(request.POST, instance=pi)
        if fm.is_valid():
            ld = fm.cleaned_data['title']
            nd = fm.cleaned_data['desc']
            '''another way of saving data in DB is fm.save()'''
            reg = blog_form(title=ld, desc=nd)
            reg.save()
            return HttpResponseRedirect('/')
      else:
        pi = Post.objects.get(pk=id)
        fm = blog_form(instance=pi)
      return render(request, 'blog/edit.html', {'form':fm})
   else:
      return HttpResponseRedirect('/login/')
   
# posting:
def posting(request):
    if request.user.is_authenticated:
      if request.method == 'POST':
          fm =blog_form(request.POST)
          if fm.is_valid():
            ld = fm.cleaned_data['title']
            nd = fm.cleaned_data['desc']
            '''another way of saving data in DB is fm.save()'''
            reg = blog_form(title=ld, desc=nd)
            reg.save()
            return HttpResponseRedirect("/dashboard/")
      else:    
       fm = blog_form()
      return render(request, 'blog/posting.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')





