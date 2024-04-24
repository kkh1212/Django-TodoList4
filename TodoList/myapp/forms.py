# myapp/forms.py

from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task']
        widgets = {'task': forms.TextInput(attrs={'class': 'form-control'})}
