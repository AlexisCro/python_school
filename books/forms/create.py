from django import forms
from django.core.validators import MinLengthValidator, MinValueValidator
from books.models import Book

class Create(forms.ModelForm):
  class Meta:
    model = Book
    fields = [
      'title',
      'isbn',
      'description',
      'published_language',
      'editor',
      'price',
      'disponibility_counter',
      'quantity',
      'page_number',
      'published_at',
      'author',
      'category'
    ]
    widgets = {
      'published_at': forms.DateTimeInput(attrs={'type': 'date'})
    }
  