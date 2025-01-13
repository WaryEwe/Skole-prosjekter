from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import BorrowingForm
from users import models
def home_view(request):
    username = request.user.username
    context = {
        'username':username,
    }
    return render(request, 'home.html', context)

def upload_view(request):
    username = request.user.username
    req_user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        borrowing_f = BorrowingForm(request.POST, request.FILES)
        if borrowing_f.is_valid():
            return redirect('home')
        else:
            return redirect('test')
            print('test')
    else:
        borrowing_f = BorrowingForm()
    context = {
        'borrowing_f':borrowing_f,
    }

    return render(request, 'upload.html', context)
