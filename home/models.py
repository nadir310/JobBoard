from django.db import models
from django.utils import timezone

class student(models.Model):
    age=models.CharField(("student age"), max_length=50,null=1)
    name=models.IntegerField(("student name"),max_length=50,null=1)
    phone=models.CharField(("student phone"),max_length=50,null=1)

    def __str__(self):
        return str(self.name)

# Create your models here.
