# books/views.py

from django.shortcuts import render
from .utils import fetch_books

def book_search(request):
    query = request.GET.get('q', '')
    books = fetch_books(query)
    return render(request, 'books/book_search.html', {'books': books})
from django.shortcuts import render

# Create your views here.
