from django.shortcuts import render

# Create your views here.

def homePage(request):
    context = {}
    return render(request, 'base/main.html', context)

def contactPage(request):
    context = {}
    return render(request, 'base/contact.html', context)
