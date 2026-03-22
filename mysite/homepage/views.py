from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Post
from .forms import SignUpForm, LoginForm, PostForm


def landing_page(request):
    """Display the landing page"""
    if request.user.is_authenticated:
        return redirect('upload')
    return render(request, 'homepage/landing.html')


def signup_view(request):
    """Handle user signup"""
    if request.user.is_authenticated:
        return redirect('upload')
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('upload')
    else:
        form = SignUpForm()
    
    return render(request, 'homepage/signup.html', {'form': form})


def login_view(request):
    """Handle user login"""
    if request.user.is_authenticated:
        return redirect('upload')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('upload')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    
    return render(request, 'homepage/login.html', {'form': form})


@login_required(login_url='login')
def logout_view(request):
    """Handle user logout"""
    logout(request)
    return redirect('landing')


@login_required(login_url='login')
def upload_post(request):
    """Handle post upload page"""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('wall')
    else:
        form = PostForm()
    
    return render(request, 'homepage/upload.html', {'form': form})


@login_required(login_url='login')
def wall_view(request):
    """Display the memory wall with all posts"""
    posts = Post.objects.all()
    return render(request, 'homepage/wall.html', {'posts': posts})


@login_required(login_url='login')
@require_POST
def add_candle(request, post_id):
    """AJAX endpoint to increment candle count"""
    post = get_object_or_404(Post, id=post_id)
    post.candle_count += 1
    post.save()
    
    return JsonResponse({
        'success': True,
        'candle_count': post.candle_count
    })
