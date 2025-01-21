from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import BorrowingForm
from users import models
from .models import BorrowingModel, RentModel
from django.contrib.auth.decorators import login_required

def home_view(request):
    borrowing = BorrowingModel.objects.all()
    username = request.user.username
    context = {
        'username':username,
        'borrowing':borrowing,
    }
    return render(request, 'home.html', context)

@login_required(login_url='login')
def rent_view(request, book_id):
    book = BorrowingModel.objects.get(id=book_id)
    rent = RentModel(borrower=request.user, borrow_material=book)
    rent.save()
    return redirect('home')




