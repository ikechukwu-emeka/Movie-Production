from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from audition.email_backend import Emailbackend
from .forms import Form
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return render(request, 'audition/index.html')
    else:
        messages.error(request, ' You Need To Login Account')
        return redirect(reverse('login'))
    
def about(request):
    return render(request, 'audition/about.html')

def dashboard(request):
    return render(request, 'audition/dashboard.html')

def sign_up(request):
    form=Form(request.POST or None, request.FILES or None)
    context={
        'title':'Sign Up',
        'form':form
        }
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request,'Successful')
            return redirect(reverse('login'))
        else:
            messages.error(request, 'Failed')
    return render(request, 'audition/sign up.html',context)

def team(request):
    return render(request, 'audition/team.html')

def services(request):
    return render(request, 'audition/services.html')

def log_in(request):
    context={
        'title':'SIGN IN'
    }
    if request.method=="POST":
        username = request.POST.get('username')
        password=request.POST.get('password')
        user=Emailbackend.authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)           
            return redirect('homepage')
        else:
            messages.error(request, 'Incorrect Input')
            return redirect(reverse('login'))
    else:
            return render(request, 'audition/login.html', context)

def log_out(request):
    logout(request)
    return redirect(reverse('dashboard'))



