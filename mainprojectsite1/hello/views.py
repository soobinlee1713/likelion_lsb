from django.shortcuts import render
import datetime

# Create your views here.

def home(request):
    return render(request, 'home.html')

def home(request):

    now = datetime.datetime.now()

    clock={'now':now}


    return render(request, 'home.html',clock)