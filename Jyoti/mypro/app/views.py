from django.contrib.sessions.models import Session
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from .forms import UserForm

# Create your views here.



def hello(request):
    return HttpResponse('<h1>Hello.........Jyoti</h1>')

def welldone(request):
    return HttpResponse('<h1> very Good......</h>')

def user(request, id = 0, name = ""):
    message = "User id = " * str(id) * " " * name
    return HttpResponse(message)

def index(request):
    msg = "Welcome to Rays....."
    return render(request, "index.html", {"message": msg})

def login(request):
    return render(request, "login.html")

def red(request):
    return redirect("/app/log/")

def registration(request):
    if request.method=="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Registration Successfully Done....")
        else:
            return HttpResponse("Please fill all the fields")

    return render(request, "Registration.html")


def create_session(request):
    request.session['name'] = 'Ashu'
    response = "<h1>Welcome To Sessions</h1><br>"
    response += "ID : {0} <br>".format(request.session.session_key)
    return HttpResponse(response)


def access_session(request):
    response = "Name : {0} <br>".format(request.session.get('name'))
    return HttpResponse(response)


def destroy_session(request):
    Session.objects.all().delete()
    return HttpResponse("Session is Destroy")



def logout(request):
    Session.objects.all().delete()
    return render(request,"loginForm.html")


def display(request):
    sql = "select * from PRO_User"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    columnName = ("id", "firstName", "lastName", "login", "password", "mobile")
    res = {
        "data": []
    }
    count = 0
    for x in result:
        print(x)
        print({columnName[i]: x[i] for i, _ in enumerate(x)})
        res["data"].append({columnName[i]: x[i] for i, _ in enumerate(x)})
    return render(request, "List.html", {"list": res['data']})


def update(request):
    if request.method=="POST":
        id = request.POST.get('id')
        fn = request.POST.get('firstName')
        ln = request.POST.get('lastName')
        e = request.POST.get('login')
        p = request.POST.get('password')
        m = request.POST.get('mobileNum')
        sql = "update PRO_User set firstName = (%s), lastName = (%s), login = (%s), password = (%s), mobile = (%s) where id = (%s)"
        data = [fn, ln, e, p, m, id]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        return HttpResponse("Update Successfully.....")
    return HttpResponse("Update Failed.....")




def edit(request, id):
    print(id)
    result = ""
    sql = "select * from PRO_User where id = (%s)"
    data = [id]
    cursor = connection.cursor()
    cursor.execute(sql, data)
    result = cursor.fetchall()
    columnName = ("id", "firstName", "lastName", "login", "password", "mobile")
    res = {
        "data": []
    }
    count = 0
    for x in result:
        print({columnName[i]: x[i] for i, _ in enumerate(x)})
        res["data"].append({columnName[i]: x[i] for i, _ in enumerate(x)})
    return render(request, "UpdateReg.html", {"list": res['data']})


def auth(request, ):
    if request.method == "POST":
        uname = request.POST.get('login')
        password = request.POST.get('password')
        sql = "select * from PRO_User where login = (%s) and password = (%s)"
        data = [uname, password]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "firstName", "lastName", "login", "password", "mobile")
        res = {
            "data": []
        }
        count = 0
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res["data"].append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return render(request, "welcome.html", {"list": res['data'], "flag":True})
    return render(request, "loginForm.html")
