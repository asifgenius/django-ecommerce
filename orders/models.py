from django.db import models
from users.models import User
from products.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    total_price = models.FloatField()
    delivery_address = models.CharField(max_length=255)
    bkash_transaction_id = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    delivery_charge = models.FloatField()  # Changed to FloatField, assuming numeric
    is_purchased = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id} by {self.user.full_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
