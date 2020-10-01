from .models import TaskO
from django.forms import ModelForm, TextInput, Textarea, DateInput, Form, IntegerField, DateField, CharField


class TaskForm(ModelForm):
    class Meta:
        model = TaskO
        fields = ["title", "task", "price", "data", "description", "image"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "task": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите тип поездки'
            }),
            "price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите цену'
            }),
            "data": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату поездки'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            })

        }


class FilterTours(Form):
    min_price = IntegerField(required=False)
    max_price = IntegerField(required=False)
    data = DateField(required=False)
    country = CharField(required=False)

