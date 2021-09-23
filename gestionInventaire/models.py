from django.db import models

# Modèle d'un produit
class Product(models.Model):
    name = models.CharField(max_length=100, blank = False)
    description = models.CharField(max_length=200)
    product_type = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places = 2, max_digits = 6)
    current_quantity = models.IntegerField()
    stock_quantity = models.IntegerField()

    def __str__(self):
        return 'Name: {0} Description: {1} Type: {2} Price: {3} Current quantity: {4} Stock quantity: {5}'.format(
            self.name, self.description, self.product_type, self.price, self.current_quantity, self.stock_quantity)

