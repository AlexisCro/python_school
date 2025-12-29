from django import forms

class Create(forms.Form):
  first_name = forms.CharField(label="Your name", max_length=150)
  last_name = forms.CharField(label="Your name", max_length=150)
  birth_date = forms.DateField()
  nationality = forms.CharField(max_length=100)