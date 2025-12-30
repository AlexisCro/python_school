from django import forms
from authors.models import Author

class Create(forms.ModelForm):
  class Meta:
    model = Author
    fields = [
      "first_name",
      "last_name",
      "birth_date",
      "nationality",
      "biographie",
      "death_date",
      "website"
    ]
    widgets = {
      'birth_date': forms.DateTimeInput(attrs={'type': 'date'}),
      'death_date': forms.DateTimeInput(attrs={'type': 'date'}),
    }
