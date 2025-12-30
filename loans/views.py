from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import Loan
from .forms.create import Create
from datetime import date
from books.models import Book

# Create your views here.
def index_view(request: HttpRequest) -> HttpResponse:
  collection = Loan.objects.all()
  return render(request, 'loans/index.html', {'collection': collection})

def new_view(request: HttpRequest) -> HttpResponse:
  form = Create()
  return render(request, 'loans/new.html', {'form': form})

def create_view(request: HttpRequest) -> HttpResponse:
  if request.method == "POST":
    form = Create(request.POST)

    if form.is_valid():
      book = get_object_or_404(Book, id=form.data['book'])
      book.disponibility_counter -= 1

      if book.disponibility_counter < 0:
        form.errors['book'] = ['The book cannot be loan because there is no more available']
        return render(request, 'loans/new.html', {'form': form})

      loan = form.save()
      loan.set_loan_time()
      loan.save()
      book.save()
      
      return render(request, 'loans/show.html', {'loan': loan})
  else:
    form = Create()
  
  return render(request, 'loans/new.html', {'form': form})

def show_views(request: HttpRequest, loan_id: int) -> HttpResponse:
  loan = get_object_or_404(Loan, id=loan_id)
  return render(request, 'loans/show.html', {'loan': loan})

def return_views(request: HttpRequest, loan_id: int) -> HttpResponse:
  collection = Loan.objects.all()
  loan = get_object_or_404(Loan, id=loan_id)
  book = loan.book

  loan.state = 'AVAILABLE'
  loan.returned_at = date.today()

  if loan.save():
    book.disponibility_counter += 1
    book.save()
  
  return render(request, 'loans/index.html', {'collection': collection})
    
