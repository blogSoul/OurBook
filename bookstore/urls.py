from django.urls import path
from . import views

urlpatterns = [
    path('', views.books , name="books"),
    path('new/', views.new_book, name="new_book"),

    path('booklist/', views.BookList.as_view(), name="book_list"),
    path('newbook/', views.BookCreate.as_view(), name="book_create"),
    path('bookdetail/<int:pk>', views.BookDetail.as_view(), name='book_detail'),
    path('update/<int:pk>', views.BookUpdate.as_view(), name='book_change'),
    path('delete/<int:pk>', views.BookDelete.as_view(), name='book_del'),

]