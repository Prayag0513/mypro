from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import *

class teacherregForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','password']
    
    def save(self):
        s=super().save(commit=False)
        s.password=make_password(self.cleaned_data['password'])
        s.save()
        return s
    
class teacherlogForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())


class teachersrForm(forms.ModelForm):
    class Meta:
        model=teachersrModel
        fields='__all__'


class studentsrForm(forms.ModelForm):
    class Meta:
        model=studentsrModel
        fields='__all__'

