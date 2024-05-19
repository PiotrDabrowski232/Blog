from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import SignUpForm
from .models import Post
from .forms import CreatePostForm
from django.shortcuts import render, get_object_or_404
from .forms import CreateCommentForm
from django.contrib.auth.decorators import login_required



def index(request):
    return redirect('post_list')


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
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            # Uzyskujemy dane z formularza
            tytul = form.cleaned_data['title']
            tresc = form.cleaned_data['description']
            image = form.cleaned_data['image']
            dostep = form.cleaned_data['dostep']
            
            # Tworzymy nowy obiekt Post i zapisujemy go
            post = Post(
                tytul=tytul,
                tresc=tresc,
                image=image,
                dostep=dostep,
                autor=request.user,
            )
            post.save()
    else:
        form = CreatePostForm()
    return render(request, './post/postForm.html', {'form': form})


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import CreatePostForm, CreateCommentForm

def index(request):
    return redirect('post_list')

def post_list(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
    else:
        posts = Post.objects.filter(dostep='Publiczny')
    return render(request, './post/post_list.html', {'posts': posts})




def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    print(post_id)
    return render(request, 'post/post_detail.html', {'post': post})


def some_view(request):
    if request.POST:
        form = CaptchaTestForm(request.POST)
        if form.is_valid():
            human = True
    else:
        form = CaptchaTestForm()

    return render(request, 'template.html', {'form':form})


from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .forms import CreateCommentForm
from .models import Post, Komentarz


from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .forms import CreateCommentForm
from .models import Post

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







