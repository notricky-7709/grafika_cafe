from dataclasses import field
from django import forms
from app_db.models import User
from django.forms import ModelForm, PasswordInput, TextInput

class CreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'level']
        
    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class':'border-bottom border-primary',
            'name':'username',
        })
        self.fields['password'].widget.attrs.update({
            'class':'border-bottom border-primary',
            'name': 'password',
        })
        
        
class EditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'level']
        
    
