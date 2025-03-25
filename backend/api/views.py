from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Post, Profile

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    # profile = Profile.objects.get(user=request.user)
    context = {
        'posts':posts,
        # 'profile':profile, 
    }
    return render(request, 'main.html', context)

def signup(request):
    if request.method == 'POST':
        try:
            fnm = request.POST.get('fnm')
            emailid = request.POST.get('emailid')
            pwd = request.POST.get('pwd')

            if User.objects.filter(username=fnm).exists():
                return render(request, 'signup.html', {'invalid': 'User Already Exists'})

            my_user = User.objects.create_user(username=fnm, email=emailid, password=pwd)
            my_user.save()

            new_profile = Profile.objects.create(user=my_user, id_user=my_user.id)
            new_profile.save()

            login(request, my_user)
            return redirect("/")

        except Exception as e:
            print(f"Error during signup: {e}")
            return render(request, 'signup.html', {'invalid': 'An error occurred during signup'})

    return render(request, 'signup.html')

def login(request):
    
    if request.method == 'POST':
        try:
            fnm = request.POST.get('fnm')
            pwd = request.POST.get('pwd')
            user = authenticate(request, username=fnm, password=pwd)

            if user is not None:
                login(request.user)
                return redirect('/')
            invalid = "Invalid Credentials"
            return render(request, 'login.html', {'invalid':invalid})
        
        except Exception as e:
            print(f"Error during login: {e}")
            return render(request, 'login.html', {'invalid': 'An error occurred during login'})
        
    return render(request, 'login.html')

def logout(request):
    logout(request)
    return redirect('/login')

def upload(request):
    if request.method == 'POST':
        user = request.user.username
        image = request.Files.get('image_upload')
        caption = request.POST['caption']
        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()
        return redirect('/')
    else: 
        return redirect('/')