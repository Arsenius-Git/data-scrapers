from django.db import models

# Create your models here.
class Get_stock(models.Model):
    stock = models.CharField(max_length=50)

    def __str__(self):
        return self.stock
