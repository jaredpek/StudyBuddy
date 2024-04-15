from django.db import models
from django.utils import timezone
from carts.models import Cart
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MinValueValidator

status_choices = [
    ("Preparing", "Preparing"),
    ("Delivering", "Delivering"),
    ("Completed", "Completed")
]

class Order(models.Model):
    '''
    The order model with relevant fields to track order status, delivery details and total price.
    '''
    order_status = models.CharField(max_length=10, default=status_choices[0][0], choices=status_choices)
    date_ordered = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart")
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=6, validators=[RegexValidator("^\d{5,10}$")])
    total = models.FloatField(validators=[MinValueValidator(0)])
    
    def __str__(self):
        return f"{self.order_status} | {self.user.username} | ${self.total} | {self.date_ordered.date()} | {self.address}, {self.postal_code}"
