from django.db import models

# Create your models here.
class Patient(models.Model):
  name = models.CharField(max_length=100)
  first_name = models.CharField(max_length=100)
  sex_at_birth = models.CharField(max_length=50)
  email = models.EmailField(max_length=254)
  notes = models.TextField()