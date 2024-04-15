from django.db import models
from products.models import Product
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Cart(models.Model):
    '''
    The cart model with relevant fields to track cart status and cart owner.
    '''
    confirmed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{'Purchased' if self.confirmed else 'Ordering'} | {self.user.username}"
    
    def get_total(self):
        '''
        Function to compute the total price of the entire cart.
        '''
        total = 0
        for item in self.items.all():
            total += (item.product.price * item.quantity)
        return total

class CartItem(models.Model):
    '''
    The cart item model that represents specific items that are in a cart, including specific products and respective quantities of specific products.
    '''
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(1)])
    
    def __str__(self):
        return f"{self.cart.user.username} | {self.product.name} | {self.quantity}"
