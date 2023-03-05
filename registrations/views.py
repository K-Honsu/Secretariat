from django.shortcuts import render, redirect
from .forms import MarryForm, ChildDedications, BirthNotifications
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.

@login_required(login_url='login')
def registrations_homepage(request):
    return render(request, 'registrations/registration_homepage.html')


@login_required(login_url='login')
def marriage(request):
    mar = MarryForm()
    if request.method == 'POST':
        mar = MarryForm(request.POST)
        if mar.is_valid():
            mar.save()
            messages.success(request, 'Details saved successfully')
            return redirect('marriage_thanks')
    context = {'mar':mar}
    return render(request, 'registrations/marriage_thanksgiving.html', context)


@login_required(login_url='login')
def birth(request):
    forms = BirthNotifications()
    if request.method == 'POST':
        forms = BirthNotifications(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Records saved successfully!')
            return redirect('all_birth')
    context = {'forms':forms}
    return render(request, 'registrations/birth_notification.html', context)


@login_required(login_url='login')
def child(request):
    form = ChildDedications()
    if request.method == 'POST':
        form = ChildDedications(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_birth')
    context = {'form':form}
    return render(request, 'registrations/child_dedication.html', context)


def abort(request):
    return render(request, 'registrations/abort.html')


def all_marriage_thanksgiving(request):
    info = MarriageThanksgiving.objects.all().order_by('-date_of_marriage')
    context = {'info':info}
    return render(request, 'registrations/all_marry.html', context)


def all_birth_notification(request):
    tab = BirthNotification.objects.all().order_by('-date_of_naming_ceremony')
    context = {'tab':tab}
    return render(request, 'registrations/all_birth.html', context)

def all_child_dedications(request):
    tabs = ChildDedication.objects.all().order_by('-time_stamp')
    context = {'tabs':tabs}
    return render(request, 'registrations/all_child.html', context)