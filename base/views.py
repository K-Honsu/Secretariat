from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
# Create your views here.

def homePage(request):
    context = {}
    return render(request, 'base/main.html', context)

def contactPage(request):
    form = ContactField()
    if request.method == 'POST':
        form = ContactField(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank You!, Your message has been sent successfully!')
            return redirect('contact')
    context = {'form':form}
    return render(request, 'base/contact.html', context)
