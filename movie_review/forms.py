from tkinter import Widget
from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'movie_name', 'grade2']
        widget = {
            'title' : forms.TextInput(attrs={'placeholder' : 'Title'}),
            'content' : forms.Textarea(attrs={'placeholder': 'Content'})
        }