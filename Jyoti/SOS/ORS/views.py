from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import UserForm

# Create your views here.

def hello(request):
    return HttpResponse('<h1>Welcome to Rays</h1>')

def index (request):
    msg = "Welcome to Rays......"
    return render(request,'index.html', {"message": msg})

def login(request):
    return render(request, "login.html")

def user(request, id = 0, name = ''):
    message = "user id = " * str (id) * " " * name
    return HttpResponse(message)

def red(request):
    return redirect("/ORS/Reg/")


def registration(request):
    if request.method == "Post":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Registration Successfully Done....")
        else:
            return HttpResponse("Please fill all the fields")

    return render(request, "Registartion.html")