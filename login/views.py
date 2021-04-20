from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import CreateForm
from .forms import DonarForm
from .models import bbank
from .models import donarreg

def homepage(request):
    return render(request, 'login/homepage.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'login/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currentbbank')
            except IntegrityError:
                return render(request, 'login/signupuser.html', {'form':UserCreationForm(), 'error':'This username is already been taken please use different username'})
        else:
            return render(request, 'login/signupuser.html', {'form':UserCreationForm(), 'error':'Password did not match'})

def currentbbank(request):
    userrequest = bbank.objects.filter(user=request.user)
    return render(request, 'login/currentbbank.html', {'userrequest':userrequest})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('homepage')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'login/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and Password did not match'})
        else:
            login(request, user)
            return redirect('currentbbank')

def donorreg(request):
    if request.method == 'GET':
        return render(request, 'login/donorreg.html', {'form':DonarForm()})
    else:
        try:
            dform = DonarForm(request.POST)
            dreg = dform.save(commit=False)
            dreg.user = request.user
            dreg.save()
            return redirect('currentbbank')
        except ValueError:
            return render(request, 'login/donorreg.html', {'form': DonarForm(), 'error': 'Incorrect data passed. Please pass the correct data'})

def createreq(request):
    if request.method == 'GET':
        return render(request, 'login/createreq.html', {'form':CreateForm()})
    else:
        try:
            form = CreateForm(request.POST)
            newreq = form.save(commit=False)
            newreq.user = request.user
            newreq.save()
            return redirect('currentbbank')
        except ValueError:
            return render(request, 'login/createreq.html', {'form':CreateForm(), 'error':'Incorrect data passed. Please pass the correct data'})

def changepass(request): 
    if request.method == 'GET':
        return render(request, 'login/changepass.html', {'form':AuthenticationForm()})
    else:
        user_changepass = authenticate(request, username=request.user, password=request.POST['password_old'])
        if user_changepass is None:
            return render(request, 'login/changepass.html', {'form':AuthenticationForm(), 'error':'Please enter correct password'})
        else:
            if request.POST['password1'] == request.POST['password2']:
                try:
                    # login(request, user)
                    user_changepass.set_password('password1')
                    user_changepass.save()
                    return redirect('currentbbank', {'form':AuthenticationForm(), 'success':'Password has successfully changed'})    
                except IntegrityError:
                    return render(request, 'login/signupuser.html', {'form':UserCreationForm(), 'error':'This username is already been taken please use different username'})
            else:
                return render(request, 'login/signupuser.html', {'form':UserCreationForm(), 'error':'New Password did not match'})

def aboutus(request):
    return render(request, 'login/aboutus.html')        

def bbuser(request):
    userrequest = bbank.objects.all()
    regdonar = donarreg.objects.all()
    return render(request, 'login/bbuser.html', {'userrequest': userrequest, 'regdonar': regdonar})

def bblogin(request):
    if request.method == 'GET':
        return render(request, 'login/bblogin.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login/bblogin.html', {'form': AuthenticationForm(), 'error': 'Username and Password did not match'})
        else:
            login(request, user)
            return redirect('bbuser')
