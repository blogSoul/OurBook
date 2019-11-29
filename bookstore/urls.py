from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.books, name="test"),
    path('', views.books_list , name="books"),
    path('new/', views.new_book, name="new_book"),
]