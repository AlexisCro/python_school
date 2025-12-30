from django import forms
from django.core.validators import MinLengthValidator, MinValueValidator
from loans.models import Loan

class Create(forms.ModelForm):
  class Meta:
    model = Loan
    fields = [
      'nbr_library_card',
      'loaner_name',
      'loaner_email',
      'state',
      'comment',
      'book'
    ]
