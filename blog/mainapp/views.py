from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignUpForm
from .models import Post


def index(request):
    all_users = User.objects.all()
    return render(request, "index.html", {"users":all_users})


def signup(request):
    form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def search(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(tytul__icontains=query)  # Przykładowe wyszukiwanie postów po tytule
    else:
        posts = Post.objects.all()  # Jeśli nie podano zapytania, zwróć wszystkie posty
    return render(request, 'search_results.html', {'posts': posts, 'query': query})

