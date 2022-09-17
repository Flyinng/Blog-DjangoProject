from django import forms
from .models import *


class Form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'imagem', 'date', 'description',
                  'category']
