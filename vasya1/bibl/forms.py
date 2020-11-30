from .models import Bibld
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class BibldForm(ModelForm):
    class Meta:
        model = Bibld
        fields = ['title_bib', 'anons_bib', 'full_text_bib', 'date_bib']
    widgets = {
        "title_bib": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Название'
        }),
        "anons_bib": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Анонс'
        }),
        "date_bib": DateTimeInput(attrs={
            'class': 'form-control',
            'placeholder': 'Дата публикации'
        }),
        "full_text_bib": Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Текст'
        })
    }