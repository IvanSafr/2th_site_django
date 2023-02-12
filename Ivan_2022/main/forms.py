from dataclasses import fields
from .models import Task
from django.forms import ModelForm, widgets, TextInput,Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'diskr']
        widgets = {'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
                   'diskr': Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
                   }
