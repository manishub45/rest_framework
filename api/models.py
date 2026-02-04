from django.db import models

# Create your models here.

<<<<<<< HEAD
class student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=100)
    gmail = models.CharField(max_length=100)

=======

class student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=100)
    city = models.CharField(max_length=100)
>>>>>>> d5cecdf1f115b278e658bde0392cb98c5ed5e38c


def __str__(self):
    return self.name
<<<<<<< HEAD

=======
    
>>>>>>> d5cecdf1f115b278e658bde0392cb98c5ed5e38c
