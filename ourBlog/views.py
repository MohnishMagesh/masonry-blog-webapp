from django.shortcuts import render
from django.http import HttpResponse

def trial(request):
    return render(request, 'trial.html')