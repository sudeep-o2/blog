from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from . models import User,Blog

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class BlogForm(ModelForm):
    class Meta:
        model=Blog
        fields='__all__'
        exclude=['host']