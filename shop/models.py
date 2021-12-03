from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    count_now = models.PositiveIntegerField(default=10)
    count = models.PositiveIntegerField(default=10)

    class Meta:
        ordering = ('name',)


class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)
    person = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
