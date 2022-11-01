from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    company = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    budget = models.IntegerField(default=0)

    def __str__(self):
        return self.name