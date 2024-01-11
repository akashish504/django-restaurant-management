from django.db import models

class PizzaOrderModel(models.Model):
    base = models.CharField(max_length=200)
    cheese = models.CharField(max_length=200)
    # toppings = ArrayField(models.CharField(max_length=255))
    create_time = models.IntegerField()
    customer_name = models.CharField(max_length=200)
    table_number = models.IntegerField()
    order_status = models.CharField(max_length=200)
    description = models.TextField()
