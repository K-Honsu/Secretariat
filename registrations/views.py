from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
# Create your views here.

def registrations_homepage(request):
    return render(request, 'registrations/registration_homepage.html')


def marriage(request):
    mar = MarryForm()
    if request.method == 'POST':
        mar = MarryForm(request.POST)
        if mar.is_valid():
            mar.save()
            messages.success(request, 'Details saved successfully')
            return redirect('registrations')
    context = {'mar':mar}
    return render(request, 'registrations/marriage_thanksgiving.html', context)
