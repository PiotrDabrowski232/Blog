from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import SignUpForm
from .models import Post
from .forms import CreatePostForm
from django.contrib.auth import get_user_model
from .models import Uzytkownik
from django.utils import timezone
from django.shortcuts import render, get_object_or_404



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
        posts = Post.objects.filter(tytul__icontains=query)  
    else:
        posts = Post.objects.all()  
    return render(request, 'search_results.html', {'posts': posts, 'query': query})


def create_post_view(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
           post = Post(
               tytul = form.cleaned_data["title"],
               tresc = form.cleaned_data["description"],
               autor = request.user
           )
           post.save()
    else:
        form = CreatePostForm()
    return render(request, './post/postForm.html', {'form': form})


def post_list(request):
    posts = Post.objects.all()
    return render(request, './post/post_list.html', {'posts': posts})



def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post/post_detail.html', {'post': post})


def some_view(request):
    if request.POST:
        form = CaptchaTestForm(request.POST)
        if form.is_valid():
            human = True
    else:
        form = CaptchaTestForm()

    return render(request, 'template.html', {'form':form})