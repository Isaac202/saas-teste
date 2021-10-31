from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=255)
    desc = models.TimeField()
    stock = models.ImageField()
    
class Category(models.Model):
    nome = models.CharField(max_length=255)
    desc = models.TimeField()