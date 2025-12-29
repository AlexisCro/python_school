from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import Book

# Create your views here.
def index_view(request: HttpRequest) -> HttpResponse:
  return HttpResponse()

def show_views(request: HttpRequest, author_id: int) -> HttpResponse:
  book = get_object_or_404(Author, id=author_id)
  return render(request, 'authors/author.html', {'author': author})
