from django.db import models

# Create your models here.

class User(models.Model):
    fname=models.CharField(max_length=70)
    lname=models.CharField(max_length=70)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=25)


    def __str__(self):
        return f"{self.fname}, {self.lname}, {self.username}, {self.password}"