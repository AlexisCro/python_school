from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import Book
from .forms.create import Create

# Create your views here.
def index_view(request: HttpRequest) -> HttpResponse:
  books = Book.objects.all()
  return render(request, 'index.html', {'books': books})

def new_view(request: HttpRequest) -> HttpResponse:
  form = Create()
  return render(request, 'new.html', {'form': form})

def create_view(request: HttpRequest) -> HttpResponse:
  if request.method == "POST":
    form = Create(request.POST)
    params = request.POST
    
    breakpoint()
    title = params.get('title', '')
    isbn = params.get('isbn', '')
    description = params.get('birth_date', '')

    if form.is_valid():
      author = Author.objects.create(
        first_name=first_name,
        last_name=last_name,
        birth_date=birth_date,
        nationality=nationality
      )

      return HttpResponseRedirect(request, 'show.html', {'author_id': author.objects.id})
    else:
      form = Create()
      return HttpResponseRedirect(request, 'new.html', {'form': form})

def show_views(request: HttpRequest, book_id: int) -> HttpResponse:
  book = get_object_or_404(Book, id=book_id)
  return render(request, 'books/book.html', {'book': book})
