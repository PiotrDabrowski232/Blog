from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Komentarz
from captcha.fields import CaptchaField

# Formularz rejestracji użytkownika
class SignUpForm(UserCreationForm):
    # Pole dla nazwy użytkownika
    username = forms.CharField(
        label='username', 
        min_length=5, 
        max_length=150, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    # Pole dla adresu email
    email = forms.EmailField(
        label='email', 
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    # Pole dla hasła
    password1 = forms.CharField(
        label='password', 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    # Pole do powtórzenia hasła
    password2 = forms.CharField(
        label='Confirm password', 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    # Pole CAPTCHA
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# Formularz tworzenia posta
class CreatePostForm(forms.ModelForm):
    # Pole dla tytułu posta
    title = forms.CharField(
        label='Tytuł', 
        min_length=5, 
        max_length=20, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    # Pole dla treści posta
    description = forms.CharField(
        label='Treść', 
        min_length=20, 
        max_length=2000, 
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    # Pole dla wyboru dostępu
    dostep = forms.ChoiceField(
        label='Dostęp', 
        choices=Post.DOSTEP_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Post
        fields = ('title', 'description', 'image', 'dostep')

# Formularz tworzenia komentarza
class CreateCommentForm(forms.ModelForm):
    # Pole dla treści komentarza
    comment = forms.CharField(
        label='Komentarz', 
        widget=forms.Textarea(attrs={'rows': 4, 'class': 'form-control'})
    )

    class Meta:
        model = Komentarz
        fields = ('comment',)
