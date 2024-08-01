from django.urls import path
from .views import *


urlpatterns = [
    path('authors/', author_list, name="author_list"),
    path('authors/<int:pk>/', author_detail, name='author-detail'),
    path('publishers/', publisher_list, name='publisher-list'),
    path('publishers/<int:pk>/', publisher_detail, name='publisher-detail'),
    path('books/', book_list, name='book-list'),
    path('books/<int:pk>/', book_detail, name='book-detail'),
]