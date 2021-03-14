from .models import ToDo
from django import forms

class TodoForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Название записи'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Содержимое записи'}))
    time = forms.DateField(widget=forms.TextInput(attrs={'type':'date', 'placeholder': 'День на момент создания записи'}))
    # slug = forms.SlugField(widget=forms.TextInput(attrs={'placeholder': 'Краткое название записи (в 1-2 словах)'}))

    class Meta:
        model = ToDo
        fields = ('title', 'content', 'time')
