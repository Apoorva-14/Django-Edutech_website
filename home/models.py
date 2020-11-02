from django.db import models

# Create your models here.

class Book(models.Model):
    sno = models.AutoField(primary_key=True)
    standard = models.IntegerField()
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    childname = models.CharField(max_length=255)


    def __str__(self):
        return self.childname + ' of class ' + str(self.standard)
