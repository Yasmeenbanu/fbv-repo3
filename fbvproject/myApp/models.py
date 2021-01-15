from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    usn=models.IntegerField()
    subjects=models.IntegerField()
    marks=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=1000)
