from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from .models import Book
from .forms.create import Create

# Create your views here.
def index_view(request: HttpRequest) -> HttpResponse:
  collection = Book.objects.all()
  return render(request, 'books/index.html', {'collection': collection})

def new_view(request: HttpRequest) -> HttpResponse:
  form = Create()
  return render(request, 'books/new.html', {'form': form})

def create_view(request: HttpRequest) -> HttpResponse:
  if request.method == "POST":
    form = Create(request.POST)

    if form.is_valid():
      book = form.save()

      return render(request, 'books/book.html', {'book': book})
  else:
    form = Create()
  
  return render(request, 'books/new.html', {'form': form})

def show_views(request: HttpRequest, book_id: int) -> HttpResponse:
  book = get_object_or_404(Book, id=book_id)
  return render(request, 'books/show.html', {'book': book})
