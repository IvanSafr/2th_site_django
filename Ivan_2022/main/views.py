from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main(request):
    return render(request, 'base.html')

def info(request):
    return render(request, 'info.html')

def us(request):
    return render(request, 'us.html')