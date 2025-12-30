from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from datetime import date, timedelta
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from books.models import Book

# Create your models here.

class Loan(models.Model):
  class State(models.TextChoices):
    LOAN = 'LOAN', _('Loan')
    AVAILABLE = 'AVAILABLE', _('Available')
      
  comment = models.CharField(max_length=350)
  nbr_library_card = models.CharField()
  loaner_name = models.CharField(max_length=50)
  
  loaner_email = models.EmailField()
  
  loaned_at=models.DateTimeField()
  should_be_returned_at = models.DateTimeField()
  returned_at = models.DateTimeField()
  
  state = models.CharField(
    choices=State.choices,
    default=State.AVAILABLE,
  )

  book = models.ForeignKey(
    Book,
    on_delete=models.PROTECT,
    related_name='loans'
  )

  def clean(self):
    if self.book.disponibility_counter == 0:
      raise ValidationError("It seems there no more book available")

    if Loan.objects.filter(loaner_name=self.loaner_name).exclude(pk=self.pk).count() >= 5:
      raise ValidationError('You cannot loan more than 5 books')

  def set_loan_time(self):
    self.should_be_returned_at = timezone.now() + timedelta(days=14)
