from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from captcha.fields import CaptchaField


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='username', min_length=5, max_length=150)
    email = forms.EmailField(label='email')
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CreatePostForm(forms.ModelForm):
    title = forms.CharField(label='title', min_length=5, max_length=20)
    description = forms.CharField(label='description', min_length=20, max_length=100)

    class Meta:
        model = Post
        fields = ('title', 'description')