from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    '''
    The product model with relevant information on a specific product.
    '''
    name = models.CharField(max_length=255)
    price = models.FloatField(validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to="images/")
    
    def __str__(self):
        return f"{self.name} | ${self.price}"
