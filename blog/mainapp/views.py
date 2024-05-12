from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignUpForm
from .models import Post
from .forms import CreatePostForm
from django.contrib.auth import get_user_model
from .models import Uzytkownik
from django.utils import timezone


def index(request):
    all_users = User.objects.all()
    return render(request, "index.html", {"users":all_users})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def search(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(tytul__icontains=query)  # Przykładowe wyszukiwanie postów po tytule
    else:
        posts = Post.objects.all()  # Jeśli nie podano zapytania, zwróć wszystkie posty
    return render(request, 'search_results.html', {'posts': posts, 'query': query})


def create_post_view(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            print("Formularz jest poprawny")  
            post = form.save(commit=False)
            User = get_user_model()  
            user_instance = User.objects.get(pk=request.user.pk) 
            print(user_instance)
            try:
                post.autor = User.objects.get(email=user_instance.email)
                post.data_utworzenia = timezone.now() 
                print(user_instance.email)
                post.save()
                print("Post został pomyślnie zapisany")  
            except Uzytkownik.DoesNotExist:
                pass
    else:
        form = CreatePostForm()
    return render(request, './post/postForm.html', {'form': form})


def post_list(request):
    posts = Post.objects.all()
    return render(request, './post/post_list.html', {'posts': posts})
