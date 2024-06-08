from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import SignUpForm, CreatePostForm, CreateCommentForm  # Import formularzy
from .models import Post, Komentarz  # Import modeli
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.http import require_POST
from captcha.fields import CaptchaField  # Import CaptchaField


# Widok przekierowujący na listę postów
def index(request):
    return redirect('post_list')


# Widok rejestracji użytkownika
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


# Widok wyszukiwania postów
def search(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(tytul__icontains=query)
    else:
        posts = Post.objects.all()
    return render(request, 'search_results.html', {'posts': posts, 'query': query})


# Widok tworzenia nowego postu
@login_required
def create_post_view(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('post_list')
    else:
        form = CreatePostForm()
    return render(request, './post/postForm.html', {'form': form})


# Widok listy postów
def post_list(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
    else:
        posts = Post.objects.filter(dostep='Publiczny')
    return render(request, './post/post_list.html', {'posts': posts})


# Widok szczegółów postu
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post/post_detail.html', {'post': post})


# Przykładowy widok, może być używany do czegoś innego
def some_view(request):
    if request.POST:
        form = CaptchaTestForm(request.POST)
        if form.is_valid():
            human = True
    else:
        form = CaptchaTestForm()

    return render(request, 'template.html', {'form': form})


# Widok wylogowania użytkownika
@require_POST
def logout_view(request):
    logout(request)
    return redirect('index')


# Widok dodawania komentarzy
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.autor = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = CreateCommentForm()
    return redirect('post_detail', post_id=post_id)


# Widok szczegółów postu z uwzględnieniem komentarzy
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Komentarz.objects.filter(post=post).order_by('-data_dodania')
    form = CreateCommentForm()
    return render(request, 'post/post_detail.html', {'post': post, 'comments': comments, 'form': form})


# Widok wyszukiwania postów
def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        if request.user.is_authenticated:
            post = Post.objects.filter(tytul__contains=searched)
        else:
            post = Post.objects.filter(dostep='Publiczny', tytul__contains=searched)

        return render(request, 'post/search.html', {'searched': searched, 'post': post})
    else:
        return render(request, 'post/search.html', {})
