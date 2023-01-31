from django.shortcuts import render

# Create your views here.

def marriage(request):
    context = {}
    return render(request, 'registrations/marriage_thanksgiving.html', context)
