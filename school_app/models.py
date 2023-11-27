from django.db import models

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=250)
    addr = models.CharField(max_length=250)
    dob = models.CharField(max_length=250)
    gender = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    dept = models.CharField(max_length=250)
    course = models.CharField(max_length=250)
    purpose = models.CharField(max_length=250)
    material = models.CharField(max_length=250)

    def __str__(self):
        return self.name