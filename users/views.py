from django.shortcuts import render, redirect
from .forms import CustomField
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def registerPage(request):
    form = CustomField()
    if request.method == 'POST':
        form = CustomField(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have been registered successfully')
            return redirect('login')
    context = {'form':form}
    return render(request, 'users/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    context = {}
    return render(request, 'users/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')