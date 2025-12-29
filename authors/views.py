from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from .forms.create import Create
from .models import Author

# Create your views here.
def index_view(request: HttpRequest) -> HttpResponse:
  authors = Author.objects.all()
  return render(request, 'index.html', {'authors': authors})

def show_view(request: HttpRequest, author_id: int) -> HttpResponse:
  author = get_object_or_404(Author, id=author_id)
  return render(request, 'show.html', {'author': author})

def new_view(request: HttpRequest) -> HttpResponse:
  form = Create()
  return render(request, 'new.html', {'form': form})

def create_view(request: HttpRequest) -> HttpResponse:
  if request.method == "POST":
    form = Create(request.POST)
    params = request.POST
    
    first_name = params.get('first_name', '')
    last_name = params.get('last_name', '')
    birth_date = params.get('birth_date', '')
    nationality = params.get('nationality', '')

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