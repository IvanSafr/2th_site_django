from django.shortcuts import render
from .forms import TaskForm
from. models import Task
from django.http import HttpResponse
# Create your views here.

def main(request):
    task = Task.objects.order_by('time')
    return render(request, 'startpage.html', {'title': "Главная сраница", 'tasks': task})

def info(request):
    return render(request, 'info.html')

def create(request):
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'create.html')
