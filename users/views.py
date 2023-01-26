from django.shortcuts import render
from .forms import CustomField
# Create your views here.

def registerPage(request):
    page = CustomField()
    context = {'page':page}
    return render(request, 'users/register.html', context)