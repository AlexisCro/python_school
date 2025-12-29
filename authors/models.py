from django.db import models

# Create your models here.
class Author(models.Model):
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

  def full_name(self):
    return f'{self.first_name} {self.last_name}'
