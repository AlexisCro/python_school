from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from datetime import date
from django.utils import timezone

from authors.models import Author
from categories.models import Category

class Book(models.Model):
  def validate_quantity_greater_or_equal_than_disponibility_counter(self):
    if self.disponibility_counter > self.quantity:
      raise ValidationError("The number of disponibility books cannot be greater than the quantity")

  def validate_published_year(value):
    current_year = date.today().year

    if value < 1450 or value > current_year:
      raise ValidationError(f'The year of published must be between 1450 and {current_year}')

  title = models.CharField(
    max_length=200,
    blank=False,
    null=False
  )

  isbn = models.CharField(
    max_length=13,
    blank=False,
    null=False,
    unique=True,
    default='0000000000000',
    validators=[MinLengthValidator(13, 'ISBN_13 must contain exactly 13 characters')] # ISBN-13 required exactly 13 characters
  )

  description= models.CharField(max_length=350, null=True)
  published_language= models.CharField(max_length=100, null=True)
  editor= models.CharField(max_length=100, null=True)

  price = models.DecimalField(
    decimal_places=2,
    max_digits=6,
    null=True
  )

  disponibility_counter = models.IntegerField(
    null=False,
    validators=[
      validate_quantity_greater_or_equal_than_disponibility_counter,
      MinValueValidator(0, 'The disponibility counter cannot be less than 0')
    ],
    default=0
  )

  quantity = models.IntegerField(
    null=False,
    default=0,
    validators=[
      validate_quantity_greater_or_equal_than_disponibility_counter,
      MinValueValidator(0, 'The quantity cannot be less than 0')
    ]
  )

  page_number = models.IntegerField(
    null=False,
    default=0,
    validators=[
      MinValueValidator(0, 'The page number cannot be less than 0')
    ]
  )

  published_at = models.DateTimeField(validators=[validate_published_year])
  created_at = models.DateTimeField(default=timezone.now())

  author = models.ForeignKey(
    Author,
    on_delete=models.PROTECT,
    related_name='books'
  )

  category = models.ForeignKey(
    Category,
    on_delete=models.PROTECT,
    related_name='categories',
    null=True
  )

  def __str__(self):
    return f"{self.title}"

  class Meta:
    # db_table = 'books'             -> permit to custom table name
    # ordering = ['-published_date'] -> default sort
    unique_together = [['title', 'author']]
