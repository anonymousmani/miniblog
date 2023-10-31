from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=150)
  desc = models.TextField()

class contact(models.Model):
  name = models.CharField(max_length=30)
  email = models.CharField(max_length=40)
  address = models.CharField(max_length=30)
  message = models.CharField(max_length=150)
