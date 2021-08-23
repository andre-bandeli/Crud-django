from django import forms
from .models import Task

class DateInput(forms.DateInput):
    input_type = 'data'

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'desc', 'data', 'active',)
        widgets = {
            'data': DateInput()
        }
    