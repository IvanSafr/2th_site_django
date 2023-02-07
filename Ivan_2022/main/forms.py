from .models import Task
from django.forms import ModelForm, widgets, TextInput

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "diskr", "time"]
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
            'diskr': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите описание'})
        }