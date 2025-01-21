from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, SignupForm
from borrowing import forms
from borrowing import models
def login_view(request):
    if request.method == 'POST':
        login_f = LoginForm(request.POST)
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, email=email, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user', username=username)
    else:
        login_f = LoginForm()
    context = {
        'login_f':login_f,
    }
    return render(request, 'login.html', context)

def signup_view(request):
    if request.method == 'POST':
        signup_f = SignupForm(request.POST)
        if signup_f.is_valid():
            signup_f.save()
            return redirect('login')
    else:
        signup_f = SignupForm()
    context = {
        'signup_f':signup_f

    }
    return render(request, 'signup.html', context)
@login_required(login_url='login')
def profile_view(request, username):
    req_user = get_object_or_404(User, username=username)
    user_model, created = User.objects.get_or_create(id=req_user.id)
    user_url = reverse('user', kwargs={'username':username})
    reserved_books = models.RentModel.objects.filter(borrower=req_user)
    if request.method == 'POST' and request.user.is_staff:
        borr_f = forms.BorrowingForm(request.POST, request.FILES)
        if borr_f.is_valid():
            borr_f_s = borr_f.save(commit=False)
            borr_f_s.borrowing_id = request.user
            borr_f_s.save()
            print('testcorr')
            return redirect('home')
        else:
            print('test')
            return redirect('user', username=username)
    else:
        borr_f = forms.BorrowingForm()

    context = {
        'req_user':req_user,
        'user_url':user_url,
        'borr_f':borr_f,
        'reserved_books':reserved_books,
    }
    return render(request, 'profile.html', context)

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')
    else:
        return redirect('home')
