from django import forms
from django.core.validators import MinLengthValidator, MinValueValidator
from categories.models import Category

class Create(forms.ModelForm):
  class Meta:
    model = Category
    fields = [
      'name',
      'description'
    ]
