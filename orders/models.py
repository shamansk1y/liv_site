from django.db import models

from shop.models import Product

class Order(models.Model):
    order_number = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    message = models.TextField(max_length=300,)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.order_number)
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.item.all())

    def save(self, *args, **kwargs):
        if not self.id:
            super().save(*args, **kwargs)  # Save the object to generate the ID
        if not self.order_number:
            self.order_number = str(100000 + self.id)
            super().save(*args, **kwargs)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.order_id)

    def get_cost(self):
        return self.price * self.quantity
