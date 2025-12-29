from django.db import models
from authors.models import Author

# Create your models here.

class Book(models.Model):
  title = models.CharField(
    max_length=200,
    blank=False,
    null=False
  )

  # TODO: create another table and the relation
  author = models.ForeignKey(Author, on_delete=models.CASCADE)

  price = models.DecimalField(
    decimal_places=2,
    max_digits=6
  )

  isbn = models.CharField(
    max_length=13,
    blank=False,
    null=False,
    unique=True
  )

  published_at = models.DateTimeField()

  def __str__(self):
    return self.title

  class Meta:
    # db_table = 'books'             -> permit to custom table name
    # ordering = ['-published_date'] -> default sort
    unique_together = [['title', 'author']]
