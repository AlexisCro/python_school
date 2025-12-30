from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Author(models.Model):
  https_validator = RegexValidator(
        regex=r'^https://',
        message="URL must be strat with 'https://'.",
        code='invalid_https'
    )

  first_name = models.CharField(
    max_length=150,
    blank=False,
    null=False
  )
  
  last_name = models.CharField(
    max_length=150,
    blank=False,
    null=False
  )

  birth_date = models.DateField()
  nationality = models.CharField(max_length=100)
  biographie = models.CharField(max_length=350, null=True)
  death_date = models.DateField(null=True)
  website = models.CharField(max_length=200, validators=[https_validator], null=True)

  def full_name(self):
    return f'{self.first_name} {self.last_name}'

  def __str__(self):
    return self.full_name

  class Meta:
    # db_table = 'books'             -> permit to custom table name
    # ordering = ['-published_date'] -> default sort
    unique_together = [['first_name', 'last_name']]
