from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import Book
from django.contrib import messages

def home(request):
    return render(request, 'home/home.html')

def syllabus(request):
    return render(request, 'home/syllabus.html')

def courses(request):
    return render(request, 'home/courses.html')

def book(request):
    if request.method == 'POST':
        standard = request.POST['standard']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        childname = request.POST['childname']
        if len(email)<3 or len(phone)<10 or len(phone)>10:
            messages.error(request, "Please fill the form correctly")
        else:
            book = Book(standard=standard, name=name, email=email, phone=phone, childname=childname)
            book.save()
            messages.info(request, "Class booked")

    return render(request, 'home/book.html')



def signupuser(request):
    if request.method == 'GET':
        return render(request, 'home/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('learn')
            except IntegrityError:
                return render(request, 'home/signupuser.html', {'form':UserCreationForm(), 'error':'This username has already been taken. Please choose a new username'})
        else:
            return render(request, 'home/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'home/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request, 'todo/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('learn')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def learn(request):
    return render(request, 'home/learn.html')


def class6(request):
    return render(request, 'home/class6.html')


def class7(request):
    return render(request, 'home/class7.html')


def class8(request):
    return render(request, 'home/class8.html')


def class9(request):
    return render(request, 'home/class9.html')


def class10(request):
    return render(request, 'home/class10.html')


def class11(request):
    return render(request, 'home/class11.html')


def class12(request):
    return render(request, 'home/class12.html')
