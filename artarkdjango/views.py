from django.shortcuts import render, redirect


#function for index page


def indexpage(request):
    return render(request, "index.html")


def userlogin(request):
    return render(request, "login.html")

def usersignup(request):
    return render(request, "sign up.html")