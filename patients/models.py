from django.db import models


# Create your models here.
class Patient(models.Model):
  last_name = models.CharField(max_length=100)
  first_name = models.CharField(max_length=100)
  sex_at_birth = models.CharField(max_length=50)
  birth_date = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False)
  email = models.EmailField(max_length=254)
  notes = models.TextField(max_length=400)

  def __str__(self):
    return self.first_name + " " + self.last_name
