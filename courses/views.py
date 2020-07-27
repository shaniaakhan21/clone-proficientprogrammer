from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Register, Enroll



def index(request):
    return render(request, 'courses/index.html')

def who(request):
    return render(request, 'courses/who.html')

def course(request):
    return render(request, 'courses/course.html')

def terms(request):
    return render(request, 'courses/terms.html')

def register(request):
    return render(request, "courses/register.html")

def registration(request):
    print("hello done successfully")
    fullname = request.POST['fullname']
    birthdate = request.POST['birthdate']
    gender = request.POST['gender']
    pincode = request.POST['pincode']
    phonenumber = request.POST['phonenumber']
    email = request.POST['email']
    gname = request.POST['gname']
    gphone = request.POST['gphone']
    city = request.POST['city']
    state = request.POST['state']
    country = request.POST['country']
    ques = request.POST['ques']

    register_info = Register(fullname=fullname, birthdate=birthdate, gender=gender,pincode=pincode, phonenumber=phonenumber, email=email, gname=gname,
    gphone=gphone, city=city, state=state, country=country, ques=ques)
    register_info.save()
    messages.success(request, 'You are now registered for demo class. Someone from our side will contact you shortly')
    return render(request, "courses/register.html")

def enroll(request):
    return render(request, "courses/enroll.html")

def enrollment(request):
    print("hello done successfully")
    fullname = request.POST['fullname']
    birthdate = request.POST['birthdate']
    gender = request.POST['gender']
    pincode = request.POST['pincode']
    phonenumber = request.POST['phonenumber']
    email = request.POST['email']
    gname = request.POST['gname']
    gphone = request.POST['gphone']
    city = request.POST['city']
    state = request.POST['state']
    country = request.POST['country']
    ques = request.POST['ques']

    enroll_info = Enroll(fullname=fullname, birthdate=birthdate, gender=gender,pincode=pincode, phonenumber=phonenumber, email=email, gname=gname,
    gphone=gphone, city=city, state=state, country=country, ques=ques)
    enroll_info.save()
    messages.success(request, 'Your enrollment is completed , do payment for the course now.')
    return render(request, "courses/enroll.html")
