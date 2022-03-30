from dataclasses import field
from pyexpat import model
from turtle import textinput
from attr import attrs

from matplotlib import widgets
from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Posts Name'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Posts Anons'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Posts Date'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Posts Text'
            })
        }

