from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import Book

# Create your views here.
def index_view(request: HttpRequest) -> HttpResponse:
  return HttpResponse()

def show_views(request: HttpRequest, book_id: int) -> HttpResponse:
  book = get_object_or_404(Book, id=book_id)
  return render(request, 'books/book.html', {'book': book})

