from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from .forms.create import Create
from .models import Author

# Create your views here.
def index_view(request: HttpRequest) -> HttpResponse:
  collection = Author.objects.all()
  return render(request, 'authors/index.html', {'collection': collection})

def show_view(request: HttpRequest, author_id: int) -> HttpResponse:
  author = get_object_or_404(Author, id=author_id)
  return render(request, 'authors/show.html', {'author': author})

def new_view(request: HttpRequest) -> HttpResponse:
  form = Create()
  return render(request, 'authors/new.html', {'form': form})

def create_view(request: HttpRequest) -> HttpResponse:
  if request.method == "POST":
    form = Create(request.POST)

    if form.is_valid():
      author = form.save()

      return render(request, 'authors/show.html', {'author': author})
    
    breakpoint()
  else:
    form = Create()
  
  return render(request, 'authors/new.html', {'form': form})
