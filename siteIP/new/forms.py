from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'role', 'skills', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО'
            }),
            "role": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Должность'
            }),
            "skills": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Навыки'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Основной текст'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            })

        }
