
from tkinter import Widget
from django import forms
from .models import Task
from django.contrib.admin import widgets

class DateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(forms.ModelForm):

    class Meta:
        completed = forms.BooleanField()
        model = Task
        fields = "__all__"
        exclude = ("user",)
        widgets = {
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'start_time': DateInput(),
            'end_time': DateInput(),

        }
        labels = {
            'title' : 'Title...',
            'description': 'Description... ',
            'priority': 'Select priority',
            'start_time': 'created date',
            'end_time': 'expiry date' ,
            'completed':'complete '
        }
       

  

        
        
        
        

    
        


         
