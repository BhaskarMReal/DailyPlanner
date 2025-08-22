from django import forms
from django.forms import TextInput, MultiWidget, CheckboxInput
from .models import Tasks

class TaskForm(forms.ModelForm):
    task = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'id': 'task'}))
    date = forms.DateField(required=True, widget=forms.DateInput(format="%d/%m%Y", attrs={"type": "date", "id": "date"}))
    important = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"id": "important"}))
    completed = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"id": "completed"}))

    class Meta:
        model = Tasks
        fields = ['task', 'date', 'important', 'completed']

    def save(self, user=None, commit=True):
        instance = super().save(commit=False)
        if user:
            instance.user = user 
        if commit:
            instance.save()
        return instance

