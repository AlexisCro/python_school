from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from .models import Category
from .forms.create import Create

# Create your views here.
def index_view(request: HttpRequest) -> HttpResponse:
  collection = Category.objects.all()
  return render(request, 'categories/index.html', {'collection': collection})

def new_view(request: HttpRequest) -> HttpResponse:
  form = Create()
  return render(request, 'categories/new.html', {'form': form})

def create_view(request: HttpRequest) -> HttpResponse:
  if request.method == "POST":
    form = Create(request.POST)

    if form.is_valid():
      category = form.save()

      return redirect('category', args=[category.id])
  else:
    form = Create()
  
  return render(request, 'categories/new.html', {"form": form})

def show_views(request: HttpRequest, ctaegory_id: int) -> HttpResponse:
  category = get_object_or_404(Category, id=category_id)
  return render(request, 'categories/category.html', {'category': category})
