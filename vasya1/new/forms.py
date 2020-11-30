from .models import Shopd
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ShopdForm(ModelForm):
    class Meta:
        model = Shopd
        fields = ['title', 'anons', 'full_text', 'date']
    widgets = {
        "title": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Название'
        }),
        "anons": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Анонс'
        }),
        "date": DateTimeInput(attrs={
            'class': 'form-control',
            'placeholder': 'Дата публикации'
        }),
        "full_text": Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Текст'
        })
    }


