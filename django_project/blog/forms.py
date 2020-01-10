from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import imgPost

class imgPostForm(forms.ModelForm):
    
    class Meta:
        model = imgPost
        fields = ['title','content']

class imgPostimgForm(forms.ModelForm):
    
    class Meta:
        model = imgPost
        fields = ['img']