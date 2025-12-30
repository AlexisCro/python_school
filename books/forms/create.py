from django import forms
from django.core.validators import MinLengthValidator, MinValueValidator
from authors.models import Author
from categories.models import Category

class Create(forms.Form):
  title = forms.CharField(
    max_length=200,
    required=True
  )

  isbn = forms.CharField(
    max_length=13,
    required=True,
    validators=[MinLengthValidator(13, 'ISBN_13 must contain exactly 13 characters')] # ISBN-13 required exactly 13 characters
  )

  description = forms.CharField(max_length=350)
  published_language = forms.CharField(max_length=100)
  editor = forms.CharField(max_length=100)

  price = forms.DecimalField()

  disponibility_counter = forms.IntegerField(
    required=True,
    validators=[
      MinValueValidator(0, 'The disponibility counter cannot be less than 0')
    ]
  )

  quantity = forms.IntegerField(
    required=True,
    validators=[
      MinValueValidator(0, 'The quantity cannot be less than 0')
    ]
  )

  page_number = forms.IntegerField(
    required=True,
    validators=[
      MinValueValidator(0, 'The page number cannot be less than 0')
    ]
  )

  published_at = forms.DateTimeField()
  created_at = forms.DateTimeField()

  author = forms.ModelChoiceField(
    queryset=Author.objects.all()
  )

  category = forms.ModelChoiceField(
    queryset=Category.objects.all()
    )
