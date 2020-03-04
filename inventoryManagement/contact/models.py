from django.db import models


# Create your models here.
class Contact(models.Model):
    firstName = models.CharField(max_length=50)
    secondName = models.CharField(max_length=50)
    PFnumber = models.CharField(max_length=50)
    Ministry = models.CharField(max_length=50)
    Department = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f'{self.firstName} {self.secondName}'

