from django.shortcuts import render, redirect
from .forms import TaskForm
from. models import Task
from django.http import HttpResponse
# Create your views here.

def main(request):
    task = Task.objects.order_by('-id')
    return render(request, 'startpage.html', {'title': "Главная сраница", 'tasks': task})

def info(request):
    return render(request, 'info.html')


def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'create.html', context)

