from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Komentarz
from captcha.fields import CaptchaField

class SignUpForm(UserCreationForm):
    username = forms.CharField(label='username', min_length=5, max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CreatePostForm(forms.ModelForm):
    title = forms.CharField(label='Tytuł', min_length=5, max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Treść', min_length=20, max_length=2000, widget=forms.Textarea(attrs={'class': 'form-control'}))
    dostep = forms.ChoiceField(label='Dostęp', choices=Post.DOSTEP_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Post
        fields = ('title', 'description', 'image', 'dostep')

class CreateCommentForm(forms.ModelForm):
    comment = forms.CharField(label='Komentarz', widget=forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}))

    class Meta:
        model = Komentarz
        fields = ('comment',)
