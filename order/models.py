from django.db import models

# Create your models here.
class Order(models.Model):
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    customer = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.product
