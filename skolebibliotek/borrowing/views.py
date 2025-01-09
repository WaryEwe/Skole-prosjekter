from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import BorrowingForm

def home_view(request):
    username = request.user.username
    context = {
        'username':username,
    }
    return render(request, 'home.html', context)

def upload_view(request):
    if request.method == 'POST':
        borrowing_f = BorrowingForm(request.POST, request.FILES)
        if borrowing_f.is_valid():
            borrowing_f.save()
            return redirect('')
        else:
            print('test')
    else:
        borrowing_f = BorrowingForm()
    context = {
        'borrowing_f':borrowing_f,
    }

    return render(request, 'upload.html', context)
