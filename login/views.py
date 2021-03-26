from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

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
    return render(request, 'login/currentbbank.html')

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
    return render(request, 'login/donorreg.html')

def createreq(request):
    return render(request, 'login/createreq.html')

def changepass(request): 
    if request.method == 'GET':
        return render(request, 'login/changepass.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password_old'])
        if user is None:
            return render(request, 'login/changepass.html', {'form':AuthenticationForm(), 'error':'Please enter correct password'})
        else:
            if request.POST['password1'] == request.POST['password2']:
                try:
                    # login(request, user)
                    user.set_password('password1')
                    user.save()
                    return redirect('currentbbank', {'form':AuthenticationForm(), 'success':'Password has successfully changed'})    
                except IntegrityError:
                    return render(request, 'login/signupuser.html', {'form':UserCreationForm(), 'error':'This username is already been taken please use different username'})
            else:
                return render(request, 'login/signupuser.html', {'form':UserCreationForm(), 'error':'New Password did not match'})

def aboutus(request):
    return render(request, 'login/aboutus.html')        
