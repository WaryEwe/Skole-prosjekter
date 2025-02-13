from django.urls import path
from . import views

urlpatterns  = [
    path('', views.home_view, name='home'),
    path('rent/<str:book_id>', views.rent_view, name='rent'),
    path('search/', views.search_book, name='search'),
]
