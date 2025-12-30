from django.db import models

class Category(models.Model):
  name = models.CharField(
    max_length=200,
    blank=False,
    null=False,
    unique=True
  )

  description= models.CharField(max_length=350)

  class Meta:
    ordering = ['-name'] # Ascending sort by default
