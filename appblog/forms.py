from django import forms
from .models import Person, Message
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BlogCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
       
        
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'



